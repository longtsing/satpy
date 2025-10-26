==========
合成图像
==========

合成图像被定义为通过处理和/或组合一个或多个数据数组（前提条件）而创建的数据数组。

合成图像在 satpy 中使用 Compositor 类生成。生成的合成图像的属性通常是前提条件的属性和用于标识它的 DataID 的键/值的组合。

内置合成器
==========

.. py:currentmodule:: satpy.composites.core

Satpy 中有许多内置的合成器可用。大多数使用 :class:`GenericCompositor` 基类，该基类处理各种图像模式（目前有 `L`、`LA`、`RGB` 和 `RGBA`）并更新属性。

以下部分总结了 Satpy 附带的合成图像，并展示了使用现有 :class:`~satpy.scene.Scene` 对象创建和使用它们的基本示例。建议将任何重复使用的合成图像配置在 YAML 配置文件中。
处理可见光或红外卫星数据的通用合成器代码可以放在名为 ``visir.yaml`` 的配置文件中。特定于仪器的合成图像可以放在相应命名的 YAML 配置文件中（例如 ``seviri.yaml`` 或 ``viirs.yaml``）。有关更多示例，请参阅 `satpy 存储库 <https://github.com/pytroll/satpy/tree/main/satpy/etc/composites>`_。

GenericCompositor
-----------------

:class:`satpy.composites.core.GenericCompositor` 类可用于创建基本的单通道和 RGB 合成图像。例如，在 Python 代码中手动构建概览合成图像可以这样做::

    >>> from satpy.composites.core import GenericCompositor
    >>> compositor = GenericCompositor("overview")
    >>> composite = compositor([local_scene[0.6],
    ...                         local_scene[0.8],
    ...                         local_scene[10.8]])

需要注意的一个重要事项是，合成图像和图像之间存在内部差异。合成图像被定义为可能具有多个波段（如 `R`、`G` 和 `B` 波段）的特殊数据集。但是，在生成图像之前，数据不会被拉伸、裁剪或进行伽马滤波。要从上述合成图像中获取图像::

    >>> from satpy.writers import get_enhanced_image
    >>> img = get_enhanced_image(composite)

.. note::

    有关合成图像创建和增强的更多详细信息，请参阅 :doc:`enhancements` 文档。
