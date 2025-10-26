==========
重采样
==========

.. automodule:: satpy.resample
   :noindex:
   :no-members:
   :no-special-members:

重采样是将卫星数据从一个地理投影或网格转换为另一个的过程。这对于组合来自不同传感器或不同分辨率的数据、创建特定地理区域的图像或将数据转换为特定的地图投影非常有用。

Satpy 使用 PyTroll 的 `pyresample` 库来执行重采样操作。它支持多种重采样方法，包括：

- **最近邻**：最快的方法，适用于分类数据
- **双线性**：在速度和质量之间取得平衡
- **椭圆加权平均**：提供最高质量的结果，但计算成本更高

基本用法
========

要重采样场景，请使用 :meth:`~satpy.scene.Scene.resample` 方法::

    >>> scn_resampled = scn.resample('eurol')

这将场景重采样到名为 'eurol' 的预定义区域。

.. note::

    有关重采样方法和高级用法的更多详细信息，请参阅完整的 :doc:`API 文档 <api/satpy.resample>`。
