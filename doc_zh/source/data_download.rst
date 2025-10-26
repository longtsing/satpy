下载数据
========

Satpy 的主要功能之一是能够读取各种卫星数据格式。但是，它目前仅提供有限的方法从远程源下载数据，这些方法仅限于 `Pytroll 示例 <https://github.com/pytroll/pytroll-examples>`_ 的演示数据。
有关详细信息，请参阅示例和 :mod:`~satpy.demo` API 文档。否则，Satpy 假定所有数据都可通过本地系统访问，无论是作为本地目录还是网络挂载的文件系统。某些使用 ``xarray`` 打开数据文件的读取器可能能够通过使用 OpenDAP 或类似协议从远程系统加载文件。

作为用户，有两种选择来访问数据：

1. 将数据下载到本地机器。
2. 连接到已经可以访问数据的远程系统。

远程系统可以访问数据的最常见情况是使用云计算服务，如 Google Cloud Platform (GCP) 或 Amazon Web Services (AWS)。另一种可能的情况是组织拥有直接广播天线，在那里他们直接从卫星或卫星任务组织（NOAA、NASA、EUMETSAT 等）接收数据。在这些情况下，数据通常作为挂载的网络文件系统可用，并且可以像正常的本地路径一样访问（加上网络通信的延迟）。

以下是一些提供可被 Satpy 读取的数据的数据源。如果您知道其他数据源，请通过创建 GitHub 问题或拉取请求告诉我们。

Amazon Web Services 上的 NOAA GOES
-----------------------------------

* `资源描述 <https://registry.opendata.aws/noaa-goes/>`__
* `数据浏览器 <http://noaa-goes16.s3.amazonaws.com/index.html>`__
* 相关读取器：``abi_l1b``

除了上述页面之外，Brian Blaylock 的 `GOES-2-Go <https://github.com/blaylockbk/goes2go>`_ Python 包对于将 GOES 数据下载到本地机器很有用。
Brian 还准备了一些使用 ``rclone`` 工具将 AWS 数据下载到本地机器的说明。这些说明可以在 `这里 <https://github.com/blaylockbk/pyBKB_v3/blob/master/rclone_howto.md>`_ 找到。

Google Cloud Platform 上的 NOAA GOES
-------------------------------------

GOES-16
^^^^^^^

* `资源描述 <https://console.cloud.google.com/marketplace/details/noaa-public/goes-16>`__
* `数据浏览器 <https://console.cloud.google.com/storage/browser/gcp-public-data-goes-16>`__
* 相关读取器：``abi_l1b``

GOES-17
^^^^^^^

* `资源描述 <https://console.cloud.google.com/marketplace/details/noaa-public/goes-17>`__
* `数据浏览器 <https://console.cloud.google.com/storage/browser/gcp-public-data-goes-17>`__
* 相关读取器：``abi_l1b``

NOAA CLASS
----------

* `数据订购 <https://www.class.ncdc.noaa.gov>`__
* 相关读取器：``viirs_sdr``

NASA VIIRS Atmosphere SIPS
---------------------------

* `资源描述 <https://sips.ssec.wisc.edu/>`__
* 相关读取器：``viirs_l1b``

EUMETSAT 数据存储和数据中心
----------------------------

* EUMETSAT 的主要数据来源是 `数据存储 <https://data.eumetsat.int/>`__
* 某些产品仍可在 `地球观测门户 <https://eoportal.eumetsat.int>`__ 上获得
