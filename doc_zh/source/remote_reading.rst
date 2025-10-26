====================
读取远程文件
====================

使用单个读取器
==============

Satpy 中的某些读取器可以通过各种传输协议直接读取数据。这是使用 `fsspec <https://filesystem-spec.readthedocs.io/en/latest/index.html>`_ 及其底层使用的各种包完成的。

例如，从公共 AWS S3 存储读取 ABI 数据可以通过以下方式完成::

    from satpy import Scene

    storage_options = {'anon': True}
    filenames = ['s3://noaa-goes16/ABI-L1b-RadC/2019/001/17/*_G16_s20190011702186*']
    scn = Scene(reader='abi_l1b', filenames=filenames, reader_kwargs={'storage_options': storage_options})
    scn.load(['true_color_raw'])

如上所述从 S3 读取需要除 `fsspec` 之外还安装 `s3fs` 库。

作为替代方案，可以使用 `fsspec 配置 <https://filesystem-spec.readthedocs.io/en/latest/features.html#configuration>`_ 提供存储选项。
对于上面的示例，配置可以保存到 `fsspec` 配置目录中的 `s3.json`（默认情况下放置在 Linux 的 `~/.config/fsspec/` 目录中）::

    {
        "s3": {
            "anon": "true"
        }
    }

.. note::

    在 `reader_kwargs` 中给出的选项仅覆盖配置文件中给出的匹配选项，其他所有内容保持原样。如果数据访问出现问题，请删除配置文件以查看是否解决了问题。


作为参考，从本地 S3 存储读取 SEVIRI HRIT 数据的方式相同::

    filenames = [
        's3://satellite-data-eumetcast-seviri-rss/H-000-MSG3*202204260855*',
    ]
    storage_options = {
        "client_kwargs": {"endpoint_url": "https://PLACE-YOUR-SERVER-URL-HERE"},
        "secret": "VERYBIGSECRET",
        "key": "ACCESSKEY"
    }
    scn = Scene(reader='seviri_l1b_hrit', filenames=filenames, reader_kwargs={'storage_options': storage_options})
    scn.load(['WV_073'])

使用 `s3.json` 中的 `fsspec` 配置，配置如下所示::

    {
        "s3": {
            "client_kwargs": {"endpoint_url": "https://PLACE-YOUR-SERVER-URL-HERE"},
            "secret": "VERYBIGSECRET",
            "key": "ACCESSKEY"
        }
    }

.. note::

    有关远程文件读取的更多详细信息，请参阅完整的 :doc:`API 文档 <api/satpy.readers>`。
