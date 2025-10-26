==========
快速入门
==========

加载和访问数据
==============

.. testsetup:: *
    >>> import sys
    >>> reload(sys)
    >>> sys.setdefaultencoding('utf8')

要处理气象卫星数据，您必须创建一个 :class:`~satpy.scene.Scene` 对象。Satpy 目前不提供下载卫星数据的接口，它假定数据已经在本地硬盘上。为了让 Satpy 访问数据，必须告诉 Scene 要读取哪些文件以及应该使用哪个 :ref:`Satpy 读取器 <reader_table>` 来读取它们：

    >>> from satpy import Scene
    >>> from glob import glob
    >>> filenames = glob("/home/a001673/data/satellite/Meteosat-10/seviri/lvl1.5/2015/04/20/HRIT/*201504201000*")
    >>> global_scene = Scene(reader="seviri_l1b_hrit", filenames=filenames)

要从文件加载数据，请使用 :meth:`Scene.load <satpy.scene.Scene.load>` 方法。打印 Scene 对象将列出当前加载的每个 :class:`xarray.DataArray` 对象：

    >>> global_scene.load(['0.8', '1.6', '10.8'])
    >>> print(global_scene)
    <xarray.DataArray 'reshape-d66223a8e05819b890c4535bc7e74356' (y: 3712, x: 3712)>
    dask.array<shape=(3712, 3712), dtype=float32, chunksize=(464, 3712)>
    Coordinates:
      * x        (x) float64 5.567e+06 5.564e+06 5.561e+06 5.558e+06 5.555e+06 ...
      * y        (y) float64 -5.567e+06 -5.564e+06 -5.561e+06 -5.558e+06 ...
    Attributes:
        orbital_parameters:   {'projection_longitude': 0.0, 'pr...
        sensor:               seviri
        platform_name:        Meteosat-11
        standard_name:        brightness_temperature
        units:                K
        wavelength:           (9.8, 10.8, 11.8)
        start_time:           2018-02-28 15:00:10.814000
        end_time:             2018-02-28 15:12:43.956000
        area:                 Area ID: some_area_name\nDescription: On-the-fly ar...
        name:                 IR_108
        resolution:           3000.40316582
        calibration:          brightness_temperature
        polarization:         None
        level:                None
        modifiers:            ()
        ancillary_variables:  []
    <xarray.DataArray 'reshape-1982d32298aca15acb42c481fd74a629' (y: 3712, x: 3712)>
    dask.array<shape=(3712, 3712), dtype=float32, chunksize=(464, 3712)>
    Coordinates:
      * x        (x) float64 5.567e+06 5.564e+06 5.561e+06 5.558e+06 5.555e+06 ...
      * y        (y) float64 -5.567e+06 -5.564e+06 -5.561e+06 -5.558e+06 ...
    Attributes:
        orbital_parameters:   {'projection_longitude': 0.0, 'pr...
        sensor:               seviri
        platform_name:        Meteosat-11
        standard_name:        toa_bidirectional_reflectance
        units:                %
        wavelength:           (0.74, 0.81, 0.88)
        start_time:           2018-02-28 15:00:10.814000
        end_time:             2018-02-28 15:12:43.956000
        area:                 Area ID: some_area_name\nDescription: On-the-fly ar...
        name:                 VIS008
        resolution:           3000.40316582
        calibration:          reflectance
        polarization:         None
        level:                None
        modifiers:            ()
        ancillary_variables:  []
    <xarray.DataArray 'reshape-e86d03c30ce754995ff9da484c0dc338' (y: 3712, x: 3712)>
    dask.array<shape=(3712, 3712), dtype=float32, chunksize=(464, 3712)>
    Coordinates:
      * x        (x) float64 5.567e+06 5.564e+06 5.561e+06 5.558e+06 5.555e+06 ...
      * y        (y) float64 -5.567e+06 -5.564e+06 -5.561e+06 -5.558e+06 ...
    Attributes:
        orbital_parameters:   {'projection_longitude': 0.0, 'pr...
        sensor:               seviri
        platform_name:        Meteosat-11
        standard_name:        toa_bidirectional_reflectance
        units:                %
        wavelength:           (1.5, 1.64, 1.78)
        start_time:           2018-02-28 15:00:10.814000
        end_time:             2018-02-28 15:12:43.956000
        area:                 Area ID: some_area_name\nDescription: On-the-fly ar...
        name:                 VIS006
        resolution:           3000.40316582
        calibration:          reflectance
        polarization:         None
        level:                None
        modifiers:            ()
        ancillary_variables:  []

Satpy 允许通过微米波长（如上所示）或通道名称加载文件数据::

    >>> global_scene.load(["VIS008", "IR_016", "IR_108"])

要查看 :class:`~satpy.scene.Scene` 对象可供加载的可用通道，请使用 :meth:`~satpy.scene.Scene.available_dataset_names` 方法：

    >>> global_scene.available_dataset_names()
    ['HRV',
     'IR_108',
     'IR_120',
     'VIS006',
     'WV_062',
     'IR_039',
     'IR_134',
     'IR_097',
     'IR_087',
     'VIS008',
     'IR_016',
     'WV_073']


要访问加载的数据，请使用波长或名称：

    >>> print(global_scene[0.8])

有关按分辨率、校准或其他高级加载方法加载数据集的更多信息，请参阅 :doc:`reading` 文档。


计算测量值和导航坐标
===================

加载后，可以从场景中的 DataArray 计算测量值，使用 .values 获取完全计算的 numpy 数组：

    >>> vis008 = global_scene["VIS008"]
    >>> vis008_meas = vis008.values

请注意，对于非常大的图像，例如半公里地球静止图像，计算的测量数组可能需要数千兆字节的内存；在这种情况下，可能更倾向于使用延迟计算和/或数据集子集。

如果存在，DataArray 的 'area' 属性可以转换为经度和纬度数组。对于某些仪器（通常是极地轨道），get_lonlats() 可能会导致数组需要额外的 .compute() 或 .values 提取。

    >>> vis008_lon, vis008_lat = vis008.attrs['area'].get_lonlats()


可视化数据
==========

要在弹出窗口中可视化加载的数据：

    >>> global_scene.show(0.8)

或者，如果在 Jupyter notebook 中工作，可以使用 :meth:`~satpy.scene.Scene.to_geoviews` 方法将场景转换为 `geoviews <https://geoviews.org>`_ 对象。geoviews 包不是基础 satpy 安装的要求，因此为了使用此功能，用户需要自己安装 geoviews 包。

    >>> import holoviews as hv
    >>> import geoviews as gv
    >>> import geoviews.feature as gf
    >>> gv.extension("bokeh", "matplotlib")
    >>> %opts QuadMesh Image [width=600 height=400 colorbar=True] Feature [apply_ranges=False]
    >>> %opts Image QuadMesh (cmap='RdBu_r')
    >>> gview = global_scene.to_geoviews(vdims=[0.6])
    >>> gview[::5,::5] * gf.coastline * gf.borders

创建新数据集
============

基于加载的数据集/通道的计算可以轻松分配给新数据集：

    >>> global_scene.load(['VIS006', 'VIS008'])
    >>> global_scene["ndvi"] = (global_scene['VIS008'] - global_scene['VIS006']) / (global_scene['VIS008'] + global_scene['VIS006'])
    >>> global_scene.show("ndvi")

在进行计算时，默认情况下，Xarray 将删除所有属性，因此需要手动复制属性。:func:`combine_metadata <satpy.dataset.metadata.combine_metadata>` 函数可以帮助完成此任务。
还可以分配其他自定义元数据。

    >>> from satpy.dataset import combine_metadata
    >>> scene['new_band'] = scene['VIS008'] / scene['VIS006']
    >>> scene['new_band'].attrs = combine_metadata(scene['VIS008'], scene['VIS006'])
    >>> scene['new_band'].attrs['some_other_key'] = 'whatever_value_you_want'

生成合成图像
============

Satpy 内置了许多合成配方，并使它们像任何其他数据集一样可加载：

    >>> global_scene.load(['overview'])

要获取当前场景的所有可用合成图像列表：

    >>> global_scene.available_composite_names()
    ['overview_sun',
     'airmass',
     'natural_color',
     'night_fog',
     'overview',
     'green_snow',
     'dust',
     'fog',
     'natural_color_raw',
     'cloudtop',
     'convection',
     'ash']

加载合成图像将加载制作该合成图像所需的所有依赖项，并在生成合成图像后卸载它们。

.. note::

    某些合成图像要求数据集具有相同的分辨率或形状。在这种情况下，必须在生成合成图像之前对 Scene 对象进行重采样（见下文）。

重采样
======

.. todo::

   解释在哪里以及如何定义新区域

在某些情况下，可能需要对数据集进行重采样，无论它们来自文件还是生成的合成图像。重采样对于将数据映射到统一网格、将输入数据限制到感兴趣区域、从一个投影更改为另一个投影或准备数据集以组合在合成图像中（见上文）很有用。有关重采样、不同重采样算法以及创建您自己的感兴趣区域的更多详细信息，请参阅 :doc:`resample` 文档。要重采样 Satpy Scene：

    >>> local_scene = global_scene.resample("eurol")

这将创建原始 ``global_scene`` 的副本，其中所有加载的数据集都重采样到内置的"eurol"区域。任何已请求但无法生成的合成图像都会在重采样后自动生成。新的 ``local_scene`` 现在可以像原始 ``global_scene`` 一样用于处理数据集、将它们保存到磁盘或在屏幕上显示它们：

    >>> local_scene.show('overview')
    >>> local_scene.save_dataset('overview', './local_overview.tif')

保存到磁盘
==========

要将所有加载的数据集保存到磁盘为 geotiff 图像：

    >>> global_scene.save_datasets()

要将所有加载的数据集保存到磁盘为 PNG 图像：

    >>> global_scene.save_datasets(writer='simple_image')

或者保存单个数据集：

    >>> global_scene.save_dataset('VIS006', 'my_nice_image.png')

数据集会自动缩放或"增强"以与输出格式兼容并提供最佳外观的图像。有关保存数据集和自定义增强的更多信息，请参阅 :doc:`writing` 文档。


切片和子集场景
==============

可以在场景级别进行数组切片，以获得导航一致的子集。请注意，这不考虑可能包含多种分辨率通道的场景，即索引切片不考虑数据集的空间分辨率。

  >>> scene_slice = global_scene[2000:2004, 2000:2004]
  >>> vis006_slice = scene_slice['VIS006']
  >>> vis006_slice_meas = vis006_slice.values
  >>> vis006_slice_lon, vis006_slice_lat = vis006_slice.attrs['area'].get_lonlats()

要一致地子集化多分辨率数据，请使用 :meth:`~satpy.scene.Scene.crop` 方法。

  >>> scene_llbox = global_scene.crop(ll_bbox=(-4.0, -3.9, 3.9, 4.0))
  >>> vis006_llbox = scene_llbox['VIS006']
  >>> vis006_llbox_meas = vis006_llbox.values
  >>> vis006_llbox_lon, vis006_llbox_lat = vis006_llbox.attrs['area'].get_lonlats()

.. _user_warnings_errors:

警告和错误
==========

在 Satpy 执行的计算过程中，您可能会看到各种警告，或者如果您启用了日志记录（请参见下面的 :ref:`troubleshooting`），则会看到警告或错误日志消息。Satpy 在处理过程中发出的一些警告源于 Satpy 所依赖的库，但由于 Satpy 进行计算的方式和 Satpy 正在处理的数据，这些警告大多是预期的。除了特殊情况外，Satpy 通常不会隐藏或忽略来自依赖项的这些警告，由用户控制他们希望如何处理它们。

Satpy 处理的许多数据数组使用 NaN 值来指示无效、掩码或质量不佳的像素。当遇到 NaN 时，某些计算或库会发出警告或错误。例如，Numpy 经常会发出如下警告::

    RuntimeWarning: invalid value encountered in multiply

在大多数情况下，这些警告是预期的。对于单个基于 Satpy 的脚本，建议使用 :func:`numpy.seterr` 或 :class:`numpy.errstate` 函数全局忽略来自 numpy 的这些警告：

.. code-block:: python

    import numpy as np
    np.seterr(invalid="ignore")

.. _troubleshooting:

故障排除
========

当出现问题时，首先要检查是否安装了最新版本的 satpy 及其依赖项。Satpy 默认会拖入一些包作为依赖项，但每个读取器和写入器都有自己的依赖项，在只进行常规 `pip install` 时可能不幸地很容易遗漏。要检查读取器和写入器的缺失依赖项，可以使用名为 :func:`~satpy.utils.check_satpy` 的实用函数：

  >>> from satpy.utils import check_satpy
  >>> check_satpy()

由于 Satpy 的工作方式，尽可能多地生成数据集，有时行为可能是意外的但没有引发异常。为了帮助排除这些情况，可以打开日志消息。要执行此操作，请在运行任何其他 Satpy 代码之前运行以下代码：

    >>> from satpy.utils import debug_on
    >>> debug_on()
