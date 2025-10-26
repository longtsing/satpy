.. _specific-readers-and-formats:

============================
特定读取器和格式
============================

在本节中，您可以找到针对选定传感器或格式的指导。

*所有*读取器的实现细节（包括独特的关键字参数）可以在 :doc:`读取器 API 文档 <api/satpy.readers>` 中找到。请注意，此文档适用于 Python 模块，可能由多个读取器实例共享。大多数共享的 Python 模块可以在 :doc:`读取器"核心"子包 <api/satpy.readers.core>` 中找到。


SEVIRI L1.5 数据
================

*旋转增强型可见光和红外成像仪（SEVIRI）是 Meteosat 第二代（MSG）的主要仪器，能够在 12 个光谱通道中观测地球。*

*1.5 级对应于已针对所有不需要的辐射和几何效应进行校正、使用标准化投影进行地理定位并经过校准和辐射线性化的图像数据。*
（摘自 EUMETSAT 文档）

Satpy 为各种 SEVIRI L1.5 数据格式提供读取器。有关通用属性，请参阅 :mod:`satpy.readers.core.seviri`。特定于格式的文档可以在这里找到：

- Native：:mod:`satpy.readers.seviri_l1b_native`
- HRIT：:mod:`satpy.readers.seviri_l1b_hrit`
- netCDF：:mod:`satpy.readers.seviri_l1b_nc`


HRIT 格式
=========

Satpy 可以读取 HRIT 格式的许多变体。通用功能在 :mod:`satpy.readers.core.hrit` 中实现。特定于格式的文档可以在这里找到：

- :mod:`SEVIRI HRIT <satpy.readers.seviri_l1b_hrit>`
- :mod:`GOES Imager HRIT <satpy.readers.goes_imager_hrit>`
- :mod:`Electro-L HRIT <satpy.readers.electrol_hrit>`
- :ref:`JMA HRIT <jma-hrit-readers>`（见下文）


.. _jma-hrit-readers:

JMA HRIT 读取器
---------------

JMA HRIT 格式在 `JMA HRIT - Mission Specific Implementation`_ 中描述。Satpy 中有三个用于此格式的读取器：

- ``jami_hrit``：用于 MTSAT-1R 上 `JAMI` 仪器的数据
- ``mtsat2-imager_hrit``：用于 MTSAT-2 上 `Imager` 仪器的数据
- ``ahi_hrit``：用于 Himawari-8/9 上 `AHI` 仪器的数据

.. note::

    有关特定读取器的更多详细信息，请参阅完整的 :doc:`API 文档 <api/satpy.readers>`。
