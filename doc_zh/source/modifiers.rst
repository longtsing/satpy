修饰符
======

修饰符是在计算合成图像之前应用于数据集的过滤器。它们至少需要一个输入（数据集）并且只有一个输出（相同的数据集，已修改）。它们可以接受其他输入数据集或参数。

修饰符在 ``$SATPY_CONFIG_PATH`` 内的 ``etc/composites`` 中的合成文件中定义。

使用某个修饰符的指令可以包含在合成定义或读取器定义中。如果在合成定义中定义，则在构造合成图像时应用。

使用内置合成图像时，Satpy 用户不需要了解修饰符的机制，因为它们会自动应用。:doc:`composites` 文档包含有关在创建新合成图像时如何应用修饰符的信息。

某些读取器读取的数据中已应用某些修饰符。在这里，读取器定义将引用 Satpy 修饰符。此标记将修饰符添加到元数据中，以防止在合成计算时再次应用它。

常用修饰符在下表中列出。有关这些修饰符的更多详细信息，请参阅链接的 API 文档。

.. list-table:: 常用修饰符
    :header-rows: 1

    * - 标签
      - 类
      - 描述
    * - ``sunz_corrected``
      - :class:`~satpy.modifiers.geometry.SunZenithCorrector`
      - 修改太阳通道的太阳天顶角以提供更平滑的图像。
    * - ``effective_solar_pathlength_corrected``
      - :class:`~satpy.modifiers.geometry.EffectiveSolarPathLengthCorrector`
      - 修改太阳通道的太阳辐射大气路径长度。
    * - ``nir_reflectance``
      - :class:`~satpy.modifiers.spectral.NIRReflectance`
      - 计算太阳和地球辐射边缘通道（3.7 µm 或 3.9 µm）的反射部分。
    * - ``nir_emissive``
      - :class:`~satpy.modifiers.spectral.NIREmissivePartFromReflectance`
      - 计算太阳和地球辐射边缘通道（3.7 µm 或 3.9 µm）的发射部分。
    * - ``rayleigh_corrected``
      - :class:`~satpy.modifiers.atmosphere.PSPRayleighReflectance`
      - 执行瑞利大气校正，通常用于真彩色图像。

.. note::

    有关所有可用修饰符的完整列表，请参阅 :doc:`API 文档 <api/satpy.modifiers>`。
