=======
写入数据
=======

Satpy 可以将数据集保存为多种格式，使用专为特定格式设计的*写入器*。
有关特定写入器可用的其他参数和功能的详细信息，请参阅下表。
大多数用例将希望使用 :meth:`~satpy.scene.Scene.save_datasets` 方法保存数据集::

    >>> scn.save_datasets(writer="simple_image")

``writer`` 参数默认使用 ``geotiff`` 写入器。
几乎所有写入器的一个常见参数是 ``filename`` 和 ``base_dir``，以帮助自动化使用自定义文件名保存文件::

    >>> scn.save_datasets(
    ...     filename="{name}_{start_time:%Y%m%d_%H%M%S}.tif",
    ...     base_dir="/tmp/my_ouput_dir")

.. versionchanged:: 0.10

    `file_pattern` 关键字参数已重命名为 `filename` 以匹配 `save_dataset` 方法的关键字参数。

.. _writer_table:

.. list-table:: Satpy 写入器
    :header-rows: 1

    * - 描述
      - 写入器名称
      - 状态
      - 示例
    * - GeoTIFF
      - :class:`geotiff <satpy.writers.geotiff.GeoTIFFWriter>`
      - 正常
      -
    * - 简单图像（PNG、JPEG 等）
      - :class:`simple_image <satpy.writers.simple_image.PillowWriter>`
      - 正常
      -
    * - NinJo TIFF（使用 ``pyninjotiff`` 包）
      - :class:`ninjotiff <satpy.writers.ninjotiff.NinjoTIFFWriter>`
      - 从 NinJo 7 开始弃用（使用 ninjogeotiff）
      -
    * - NetCDF（标准 CF）
      - :class:`cf <satpy.writers.cf_writer.CFWriter>`
      - Beta
      - :mod:`使用示例 <satpy.writers.cf_writer>`
    * - AWIPS II 平铺 NetCDF4
      - :class:`awips_tiled <satpy.writers.awips_tiled.AWIPSTiledWriter>`
      - Beta
      -
    * - 带 NinJo 标签的 GeoTIFF（从 NinJo 7 开始）
      - :class:`ninjogeotiff <satpy.writers.ninjogeotiff.NinJoGeoTIFFWriter>`
      - Beta
      -

可用写入器
==========

要获取可用写入器的列表，请使用 `available_writers` 函数::

    >>> from satpy import available_writers
    >>> available_writers()


使用用户提供的颜色映射进行着色和调色板化
========================================

.. note::

    将来此功能将添加到 ``Scene`` 对象中。

可以创建单通道"合成图像"，然后使用用户自己的颜色映射进行着色。颜色映射是形状为 (num, 3) 的 Numpy 数组，请参阅下面的示例如何创建映射文件。

此示例创建一个 2 色颜色映射，我们在定义的温度范围之间插值颜色。超出这些限制的图像将被裁剪。

.. note::

    有关写入数据和高级用法的更多详细信息，请参阅完整的 :doc:`API 文档 <api/satpy.writers>`。
