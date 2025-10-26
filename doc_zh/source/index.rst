==================
Satpy 文档
==================

Satpy 是一个用于读取、处理和写入遥感地球观测卫星仪器数据的 Python 库。Satpy 为用户提供读取器，可将各种文件格式的地球物理参数转换为通用的 Xarray :class:`~xarray.DataArray` 和 :class:`~xarray.Dataset` 类，以便更轻松地与其他科学 Python 库实现互操作。有关可用读取器的完整列表，请参阅 :ref:`reader_table`。
Satpy 还提供了通过组合来自多个仪器波段或产品的数据来创建 RGB（红/绿/蓝）图像和其他合成类型的接口。提供了各种大气校正和视觉增强功能，以提高输出图像的实用性和质量。输出数据可以写入多种输出文件格式，如 PNG、GeoTIFF 和 CF 标准 NetCDF 文件。Satpy 还允许用户将数据重采样到地理投影网格（区域）。Satpy 由开源的 `Pytroll <http://pytroll.github.io/>`_ 小组维护。

Satpy 库作为 Pytroll 小组维护的其他库之上的高级抽象层，包括：

- `pyresample <http://pyresample.readthedocs.io/en/latest/>`_
- `pyspectral <https://pyspectral.readthedocs.io/en/latest/>`_
- `trollimage <http://trollimage.readthedocs.io/en/latest/>`_
- `pycoast <https://pycoast.readthedocs.io/en/latest/>`_
- `pydecorate <https://pydecorate.readthedocs.io/en/latest/>`_
- `python-geotiepoints <https://python-geotiepoints.readthedocs.io/en/latest/>`_
- `pyninjotiff <https://github.com/pytroll/pyninjotiff>`_

访问 Satpy project_ 页面获取源代码和下载。

Satpy 设计为易于扩展，通过创建插件（读取器、合成器、写入器等）来支持任何地球观测卫星。此页面底部的表格显示了基础 Satpy 安装所支持的输入格式。

.. note::

    Satpy 的接口不保证稳定，可能会发生变化，直到 1.0 版本时向后兼容性将成为主要关注点。

.. _project: http://github.com/pytroll/satpy


获取帮助
========

在安装或使用 Satpy 时遇到问题？请随时在 PyTroll 小组的任何联系方式中提问，联系方式见 `这里 <https://pytroll.github.io/#getting-in-touch>`_，或在 `Satpy 的 GitHub 页面 <https://github.com/pytroll/satpy/issues>`_ 上提交问题。

文档目录
========

.. toctree::
    :maxdepth: 2

    overview
    install
    config
    data_download
    examples/index
    quickstart
    reading
    remote_reading
    composites
    resample
    enhancements
    writing
    multiscene
    dev_guide/index
    readers_formats

.. toctree::
    :maxdepth: 1

    Satpy API <api/modules>
    faq
    发布说明 <https://github.com/pytroll/satpy/blob/main/CHANGELOG.md>
    安全策略 <https://github.com/pytroll/satpy/blob/main/SECURITY.md>


.. note::

    请注意，曾经放在这里的读取器表格已移至"阅读"部分：:ref:`reader_table`。

索引和表格
==========

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
