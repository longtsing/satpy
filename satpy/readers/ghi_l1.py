#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright (c) 2019 Satpy developers
#
# This file is part of satpy.
#
# satpy is free software: you can redistribute it and/or modify it under the
# terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# satpy is distributed in the hope that it will be useful, but WITHOUT ANY
# WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR
# A PARTICULAR PURPOSE.  See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# satpy.  If not, see <http://www.gnu.org/licenses/>.
"""Geostationary High-speed Imager reader for the Level_1 HDF format.

This instrument is aboard the Fengyun-4B satellite. No document is available to describe this
format is available, but it's broadly similar to the co-flying AGRI instrument.

"""

import logging
from datetime import datetime

import dask.array as da
import numpy as np
from pyproj import Proj
import xarray as xr

from satpy.readers._geos_area import get_area_definition
from satpy.readers.hdf5_utils import HDF5FileHandler

logger = logging.getLogger(__name__)

# info of 500 m, 1 km, 2 km and 4 km data
RESOLUTION_LIST = [250, 500, 1000, 2000]
_COFF_list = [21982.5, 10991.5, 5495.5, 2747.5]
_CFAC_list = [163730198.0, 81865099.0, 40932549.0, 20466274.0]
_LOFF_list = [21982.5, 10991.5, 5495.5, 2747.5]
_LFAC_list = [163730198.0, 81865099.0, 40932549.0, 20466274.0]
_NLINE_list = [43960/2., 21980/2., 10990/2., 5495/2.]
_NCOLS_list = [43960/2., 21980/2., 10990/2., 5495/2.]

PLATFORM_NAMES = {'FY4B': 'FY-4B',
                  'FY4C': 'FY-4C'}

CHANS_ID = 'NOMChannel'
SAT_ID = 'NOMSatellite'
SUN_ID = 'NOMSun'


def scale(dn, slope, offset):
    """Convert digital number (DN) to calibrated quantity through scaling.

    Args:
        dn: Raw detector digital number
        slope: Slope
        offset: Offset

    Returns:
        Scaled data

    """
    ref = dn * slope + offset
    ref = ref.clip(min=0)
    ref.attrs = dn.attrs

    return ref


def apply_lut(data, lut):
    """Calibrate digital number (DN) by applying a LUT.

    Args:
        data: Raw detector digital number
        lut: the look up table
    Returns:
        Calibrated quantity
    """
    # append nan to the end of lut for fillvalue
    lut = np.append(lut, np.nan)
    data.data = da.where(data.data > lut.shape[0], lut.shape[0] - 1, data.data)
    res = data.data.map_blocks(_getitem, lut, dtype=lut.dtype)
    res = xr.DataArray(res, dims=data.dims,
                       attrs=data.attrs, coords=data.coords)

    return res


def _getitem(block, lut):
    return lut[block]


class HDF_GHI_L1(HDF5FileHandler):
    """AGRI l1 file handler."""

    def __init__(self, filename, filename_info, filetype_info):
        """Init filehandler."""
        super(HDF_GHI_L1, self).__init__(filename, filename_info, filetype_info)

    def get_dataset(self, dataset_id, ds_info):
        """Load a dataset."""
        ds_name = dataset_id['name']
        logger.debug('Reading in get_dataset %s.', ds_name)
        file_key = ds_info.get('file_key', ds_name)
        if CHANS_ID in file_key:
            file_key = f'Data/{file_key}'
        elif SUN_ID in file_key or SAT_ID in file_key:
            file_key = f'Navigation/{file_key}'
        data = self.get(file_key)
        if data.ndim >= 2:
            data = data.rename({data.dims[-2]: 'y', data.dims[-1]: 'x'})

        data = self.calibrate(data, ds_info, ds_name, file_key)

        self.adjust_attrs(data, ds_info)

        return data

    def adjust_attrs(self, data, ds_info):
        """Adjust the attrs of the data."""
        satname = PLATFORM_NAMES.get(self['/attr/Satellite Name'], self['/attr/Satellite Name'])
        data.attrs.update({'platform_name': satname,
                           'sensor': self['/attr/Sensor Identification Code'].lower(),
                           'orbital_parameters': {
                               'satellite_nominal_latitude': self['/attr/NOMSubSatLat'].item(),
                               'satellite_nominal_longitude': self['/attr/NOMSubSatLon'].item(),
                               'satellite_nominal_altitude': self['/attr/NOMSatHeight'].item()}})
        data.attrs.update(ds_info)
        # remove attributes that could be confusing later
        data.attrs.pop('FillValue', None)
        data.attrs.pop('Intercept', None)
        data.attrs.pop('Slope', None)

    def calibrate(self, data, ds_info, ds_name, file_key):
        """Calibrate the data."""
        # Check if calibration is present, if not assume dataset is an angle
        calibration = ds_info.get('calibration')
        # Return raw data in case of counts or no calibration
        if calibration in ('counts', None):
            data.attrs['units'] = ds_info['units']
            ds_info['valid_range'] = data.attrs['valid_range']
        elif calibration == 'reflectance':
            channel_index = int(file_key[-2:]) - 1
            data = self.calibrate_to_reflectance(data, channel_index, ds_info)

        elif calibration == 'brightness_temperature':
            data = self.calibrate_to_bt(data, ds_info, ds_name)
        elif calibration == 'radiance':
            raise NotImplementedError("Calibration to radiance is not supported.")
        # Apply range limits, but not for counts or we convert to float!
        if calibration != 'counts':
            data = data.where((data >= min(data.attrs['valid_range'])) &
                              (data <= max(data.attrs['valid_range'])))
        else:
            data.attrs['_FillValue'] = data.attrs['FillValue'].item()
        return data

    def calibrate_to_reflectance(self, data, channel_index, ds_info):
        """Calibrate to reflectance [%]."""
        logger.debug("Calibrating to reflectances")
        # using the corresponding SCALE and OFFSET
        cal_coef = 'Calibration/CALIBRATION_COEF(SCALE+OFFSET)'
        num_channel = self.get(cal_coef).shape[0]
        if num_channel == 1:
            # only channel_2, resolution = 500 m
            channel_index = 0
        data.attrs['scale_factor'] = self.get(cal_coef)[channel_index, 0].values.item()
        data.attrs['add_offset'] = self.get(cal_coef)[channel_index, 1].values.item()
        data = scale(data, data.attrs['scale_factor'], data.attrs['add_offset'])
        data *= 100
        ds_info['valid_range'] = (data.attrs['valid_range'] * data.attrs['scale_factor'] + data.attrs['add_offset'])
        ds_info['valid_range'] = ds_info['valid_range'] * 100
        return data

    def calibrate_to_bt(self, data, ds_info, ds_name):
        """Calibrate to Brightness Temperatures [K]."""
        logger.debug("Calibrating to brightness_temperature")
        lut_key = f'Calibration/{ds_info.get("lut_key", ds_name)}'
        lut = self.get(lut_key)
        # the value of dn is the index of brightness_temperature
        data = apply_lut(data, lut)
        ds_info['valid_range'] = lut.attrs['valid_range']
        return data

    def get_area_def(self, key):
        """Get the area definition."""
        # Coordination Group for Meteorological Satellites LRIT/HRIT Global Specification
        # https://www.cgms-info.org/documents/cgms-lrit-hrit-global-specification-(v2-8-of-30-oct-2013).pdf
        res = key['resolution']
        pdict = {}

        c_lats = self.file_content['/attr/Corner-Point Latitudes']
        c_lons = self.file_content['/attr/Corner-Point Longitudes']

        p1 = (c_lons[0], c_lats[0])
        p2 = (c_lons[1], c_lats[1])
        p3 = (c_lons[2], c_lats[2])
        p4 = (c_lons[3], c_lats[3])

        init_line = self.file_content['/attr/Begin Line Number']
        end_line = self.file_content['/attr/End Line Number']
        init_col = self.file_content['/attr/Begin Pixel Number']
        end_col = self.file_content['/attr/End Pixel Number']

        mid_line = (init_line + end_line) / 2.
        mid_col = (init_col + end_col) / 2.

      #  pdict['init_line'] = init_line
      #  pdict['end_line'] = end_line
      #  pdict['init_col'] = init_col
      #  pdict['end_col'] = end_col

      #  pdict['mid_line'] = mid_line
      #  pdict['mid_col'] = mid_col

        pdict['coff'] = _COFF_list[RESOLUTION_LIST.index(res)]
        pdict['loff'] = -_LOFF_list[RESOLUTION_LIST.index(res)]
        pdict['cfac'] = _CFAC_list[RESOLUTION_LIST.index(res)]
        pdict['lfac'] = _LFAC_list[RESOLUTION_LIST.index(res)]
        pdict['a'] = self.file_content['/attr/Semi_major_axis'] * 1E3  # equator radius (m)
        pdict['b'] = self.file_content['/attr/Semi_minor_axis'] * 1E3  # equator radius (m)
        pdict['h'] = self.file_content['/attr/NOMSatHeight'] * 1E3  # the altitude of satellite (m)

        pdict['ssp_lon'] = float(self.file_content['/attr/NOMSubSatLon'])
        pdict['nlines'] = self.file_content['/attr/RegLength']
        pdict['ncols'] = self.file_content['/attr/RegWidth']

        pdict['col_step_ang'] = self.file_content['/attr/dSamplingAngle'] * 1e-6
        pdict['line_step_ang'] = self.file_content['/attr/dSteppingAngle'] * 1e-6

        pdict['scandir'] = 'N2S'

        b250 = ['C01']
        b500 = ['C02', 'C03', 'C04', 'C05', 'C06']

        pdict['a_desc'] = "AGRI {} area".format(self.filename_info['observation_type'])

        if key['name'] in b250:
            pdict['a_name'] = self.filename_info['observation_type'] + '_250m'
            pdict['p_id'] = 'FY-4A, 250m'
        elif key['name'] in b500:
            pdict['a_name'] = self.filename_info['observation_type'] + '_500m'
            pdict['p_id'] = 'FY-4A, 500m'
        else:
            pdict['a_name'] = self.filename_info['observation_type'] + '_2000m'
            pdict['p_id'] = 'FY-4A, 2000m'

        pdict['nlines'] = pdict['nlines'] - 1
        pdict['ncols'] = pdict['ncols'] - 1

        proj_dict = {'a': pdict['a'],
                     'lon_0': pdict['ssp_lon'],
                     'h': pdict['h'],# - pdict['a'],
                     'rf': 1 / (pdict['a'] / pdict['b'] - 1),
                     'proj': 'geos',
                     'units': 'm',
                     'sweep': 'x'}
        p = Proj(proj_dict)
        o1 = (p(p1[0], p1[1]))
        o2 = (p(p2[0], p2[1]))
        o3 = (p(p3[0], p3[1]))
        o4 = (p(p4[0], p4[1]))

        lons = (o1[0], o2[0], o3[0], o4[0])
        lats = (o1[1], o2[1], o3[1], o4[1])

        pdict['nlines'] = pdict['nlines'] + 1
        pdict['ncols'] = pdict['ncols'] + 1
        area = get_area_definition(pdict, (lons[2], lats[3], lons[3], lats[2]))

        return area

    @property
    def start_time(self):
        """Get the start time."""
        start_time = self['/attr/Observing Beginning Date'] + 'T' + self['/attr/Observing Beginning Time'] + 'Z'
        return datetime.strptime(start_time, '%Y-%m-%dT%H:%M:%S.%fZ')

    @property
    def end_time(self):
        """Get the end time."""
        end_time = self['/attr/Observing Ending Date'] + 'T' + self['/attr/Observing Ending Time'] + 'Z'
        return datetime.strptime(end_time, '%Y-%m-%dT%H:%M:%S.%fZ')
