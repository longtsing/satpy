示例
====

Satpy 示例以 Jupyter Notebook 的形式提供，位于 `pytroll-examples <https://github.com/pytroll/pytroll-examples/tree/main/satpy>`_ git 存储库中。一些示例在本文档的单独页面中有更详细的描述。它们包括 python 代码、PNG 图像以及示例正在做什么的描述。以下是一些示例的列表和简要摘要。其他示例可以在上面提到的存储库中找到，或作为本文档各部分的说明。

.. toctree::
    :hidden:
    :maxdepth: 1

    fci_l1c_natural_color
    vii_l1b_nc

.. list-table::
    :header-rows: 1

    * - 名称
      - 描述
    * - `MSG 数据快速入门 <https://nbviewer.jupyter.org/github/pytroll/pytroll-examples/blob/main/satpy/hrit_msg_tutorial.ipynb>`_
      - Satpy 加载和处理卫星数据的快速入门，本示例使用 MSG 数据
    * - `Cartopy 绘图 <https://nbviewer.jupyter.org/github/pytroll/pytroll-examples/blob/main/satpy/Cartopy%20Plot.ipynb>`_
      - 使用 Cartopy 和 matplotlib 绘制单个 VIIRS SDR 粒度
    * - `Himawari-8 AHI 真彩色 <https://nbviewer.jupyter.org/github/pytroll/pytroll-examples/blob/main/satpy/ahi_true_color_pyspectral.ipynb>`_
      - 从 Himawari-8 AHI 数据生成并重采样瑞利校正的真彩色 RGB
    * - `Sentinel-3 OLCI 真彩色 <https://nbviewer.jupyter.org/github/pytroll/pytroll-examples/blob/main/satpy/OLCI%20L1B.ipynb>`_
      - 从 Sentinel-3 OLCI L1B 数据创建真彩色图像
    * - :doc:`FCI L1C 自然彩色 <fci_l1c_natural_color>`
      - 使用 FCI L1C 数据创建自然彩色合成图像
    * - :doc:`VII L1B NetCDF <vii_l1b_nc>`
      - 读取和处理 VII L1B NetCDF 数据

.. note::

    有关更多示例和教程，请访问 `pytroll-examples 存储库 <https://github.com/pytroll/pytroll-examples>`_。
