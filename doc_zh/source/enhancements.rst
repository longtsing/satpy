增强
====

增强是 Satpy 准备数据以保存为输出图像格式的方式。增强函数通常在一组限制之间线性、对数尺度或其他方式拉伸（又称缩放）数据，以便更容易理解数据。增强通常作为类似图像输出的 :doc:`写入 <writing>` 过程的一部分自动应用。请注意，如果写入器期望保存"原始"数据，则并非所有写入器都会应用增强。增强也可以手动应用。有关更多信息，请参阅 :ref:`manual_enhancements` 部分。

配置增强
--------

Satpy 增强在 YAML 文件中配置，类似于其他 Satpy 组件。它们位于 ``$SATPY_CONFIG_PATH/enhancements/`` 目录中。此基本目录可以自定义并包含用户定义的目录。有关更多信息，请参阅 :ref:`component_configuration`。

增强可以在始终为所有数据加载的 ``generic.yaml`` 文件中定义，也可以在与正在处理的 ``DataArray`` 的 ``.attrs["sensor"]`` 元数据相对应的特定于仪器的文件（例如 ``seviri.yaml``）中定义。首先加载通用增强，然后加载特定于传感器的增强文件。

增强 YAML 格式
^^^^^^^^^^^^^^

增强 YAML 格式以 ``enhancements:`` 名称开头，后跟一系列增强"部分"。示例文件可能如下所示：

.. code-block:: yaml

   enhancements:
     default:
       operations:
       - name: stretch
         method: !!python/name:satpy.enhancements.contrast.stretch
         kwargs: {stretch: linear}
     reflectance_default:
       standard_name: toa_bidirectional_reflectance
       operations:
       - name: linear_stretch
         method: !!python/name:satpy.enhancements.contrast.stretch
         kwargs: {stretch: 'crude', min_stretch: 0.0, max_stretch: 100.}
       - name: gamma
         method: !!python/name:satpy.enhancements.contrast.gamma
         kwargs: {gamma: 1.5}
     overview:
       standard_name: overview
       operations:
         - name: inverse
           method: !!python/name:satpy.enhancements.contrast.invert
           args: [False, False, True]
         - name: stretch
           method: !!python/name:satpy.enhancements.contrast.stretch
           kwargs:
             stretch: linear
         - name: gamma
           method: !!python/name:satpy.enhancements.contrast.gamma
           kwargs: {gamma: 1.8}

.. note::

    有关增强配置和高级用法的更多详细信息，请参阅完整的 :doc:`API 文档 <api/satpy.enhancements>`。
