远程文件支持
============

本指南介绍如何在 Satpy 读取器中添加对远程文件系统的支持。

使用 FSSpec
===========

Satpy 使用 `fsspec` 库来支持从各种远程文件系统读取数据，包括：

* Amazon S3
* Google Cloud Storage
* Azure Blob Storage
* HTTP/HTTPS
* FTP

在读取器中实现远程文件支持
==========================

要在读取器中添加远程文件支持：

1. 确保读取器使用 fsspec 兼容的文件打开方法
2. 支持 `storage_options` 参数
3. 处理远程 URL 模式

示例
====

.. code-block:: python

    from satpy.readers import FSFile

    class MyReader(FileYAMLReader):
        def __init__(self, filenames, reader_kwargs=None, **kwargs):
            storage_options = reader_kwargs.get('storage_options', {})
            # 使用 storage_options 进行文件访问

.. note::

    有关详细信息，请参阅 fsspec 文档和 Satpy 中的现有实现。
