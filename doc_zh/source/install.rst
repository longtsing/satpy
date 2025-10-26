=========================
安装说明
=========================

Satpy 可以从 conda-forge（通过 conda）、PyPI（通过 pip）或从源代码（通过 pip+git）获取。以下说明展示了如何安装 Satpy 的稳定版本。有关开发/不稳定版本，请参阅 :ref:`devinstall`。

基于 Conda 的安装
==================

Satpy 可以通过从 conda-forge 频道安装包来安装到 conda 环境中。如果您还没有访问 conda 安装的权限，我们建议安装 `miniconda <https://docs.conda.io/en/latest/miniconda.html>`_ 以获得最小和最简单的安装。

以下命令将使用 ``-c conda-forge`` 来确保从 conda-forge 频道下载包。或者，您可以通过运行以下命令告诉 conda 始终使用 conda-forge：

.. code-block:: bash

    $ conda config --add channels conda-forge

在新的 conda 环境中
-------------------

我们建议为您使用 Satpy 的工作创建一个单独的环境。要创建一个新环境并一次性安装 Satpy，您可以运行：

.. code-block:: bash

    $ conda create -c conda-forge -n my_satpy_env python satpy

然后您必须激活环境，以便任何将来的 python 或 conda 命令将使用此环境。

.. code-block::

    $ conda activate my_satpy_env

这种创建已安装 Satpy（以及可选的其他包）的环境的方法通常比创建环境然后再安装 Satpy 和其他包更快（请参阅下面的部分）。

在现有环境中
------------

.. note::

    建议在首次探索 Satpy 时，创建一个专门用于此目的的新环境，而不是修改用于其他工作的环境。

如果您已经有一个 conda 环境，它已被激活，并且想要将 Satpy 安装到其中，请运行以下命令：

.. code-block:: bash

    $ conda install -c conda-forge satpy

.. note::

    Satpy 仅自动安装处理最常见用例所需的依赖项。如果遇到导入错误，可能需要使用 conda 或 pip 安装其他依赖项。要检查您的安装，请使用 :ref:`此处 <troubleshooting>` 讨论的 ``check_satpy`` 函数。

基于 Pip 的安装
===============

Satpy 可从 Python 包索引（PyPI）获得。可以使用 `Virtualenv <http://pypi.python.org/pypi/virtualenv>`_ 为 `satpy` 创建沙箱环境。

要安装 `satpy` 包和最少量的 python 依赖项：

.. code-block:: bash

    $ pip install satpy

其他依赖项可以作为"额外"安装，并按读取器、写入器或添加的功能分组。可用的额外内容可以在 `pyproject.toml <https://github.com/pytroll/satpy/blob/main/pyproject.toml>`_ 文件中找到。
它们可以单独安装：

.. code-block:: bash

    $ pip install "satpy[viirs_sdr]"

或者一次性全部安装，尽管由于依赖项数量庞大，不建议这样做：

.. code-block:: bash

    $ pip install "satpy[all]"

Ubuntu 系统 Python 安装
========================

要在 Ubuntu 系统上安装 Satpy，我们建议使用虚拟环境将 Satpy 及其依赖项与系统其余部分分开。请注意，这些说明需要使用"sudo"权限，这可能不是所有用户都可以使用的，并且可能非常危险。以下说明尝试使用 Ubuntu `apt` 包管理器安装一些 Satpy 依赖项以简化安装。将 `/path/to/pytroll-env` 替换为要创建的环境。

.. code-block:: bash

    $ sudo apt-get install python-pip python-gdal
    $ sudo pip install virtualenv
    $ virtualenv /path/to/pytroll-env
    $ source /path/to/pytroll-env/bin/activate
    $ pip install satpy
