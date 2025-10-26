=======
读取数据
=======

.. todo::

    如何从 NWCSAF 软件读取云产品。（单独的文档？）

Satpy 通过*读取器*的概念支持从多种输入文件格式和方案读取和加载数据。每个读取器支持特定类型的输入数据。:class:`~satpy.scene.Scene` 对象通过其 ``load`` 方法提供了一个简单的界面，围绕所有这些各种格式的复杂性。以下部分描述了可以加载、请求或添加数据到 Scene 对象的不同方式。

可用读取器
==========

有关 Satpy 中当前可用的读取器，请参阅 :ref:`reader_table`。
此外，要获取可用读取器的列表，您可以使用 `available_readers` 函数。默认情况下，它返回可用读取器的名称。
要返回其他读取器信息，请使用 `available_readers(as_dict=True)`::

    >>> from satpy import available_readers
    >>> available_readers()


.. _reader_table:

读取器表
--------

.. include:: reader_table.rst

.. _Status Description:
.. note::

    状态描述：

    已失效（Defunct）
        读取器很可能不起作用。即使起作用，也很有可能存在错误和/或性能问题（例如，尚未移植到 dask/xarray）。未来的发展不明确。鼓励用户做出贡献（请参阅 :doc:`dev_guide/CONTRIBUTING` 部分和/或在 Slack 上获取帮助或通过打开 Github 问题）。

    Alpha
        这表示早期开发状态。读取器功能正常并实现了一些或所有标称功能。可能存在错误。不保证结果的准确性。使用风险自负。

    Beta
        这表示最终开发状态。读取器功能正常并实现所有标称功能。结果应该是可靠的，但可能存在错误。积极鼓励用户测试和报告错误。

    正常（Nominal）
        这表示已完成状态。读取器功能正常，很可能不会引入新功能。它已经过测试，没有已知的错误。

特定读取器的文档
----------------

有关特定于读取器的文档，请参阅 :ref:`specific-readers-and-formats`

过滤加载的文件
==============

即将推出...

加载数据
========

Satpy 中的数据集由在数据加载期间设置的某些元数据片段标识。这些包括 `name`、`wavelength`、`calibration`、`resolution`、`polarization` 和 `modifiers`。通常，一旦创建了 ``Scene``，通过 `name` 或 `wavelength` 请求数据集就足够了::

    >>> from satpy import Scene
    >>> scn = Scene(reader="seviri_l1b_hrit", filenames=filenames)
    >>> scn.load([0.6, 0.8, 10.8])

.. note::

    有关数据加载和高级用法的更多详细信息，请参阅完整的 :doc:`API 文档 <api/satpy>`。
