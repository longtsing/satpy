=================
开发者指南
=================

以下部分将介绍如何设置开发环境、对代码进行更改以及测试它们是否有效。有关入门和贡献者期望的更多信息，请参阅 :doc:`CONTRIBUTING` 部分。开发者的其他信息可以在下面列出的页面中找到。

.. toctree::
    :maxdepth: 1

    CONTRIBUTING
    xarray_migration
    custom_reader
    remote_file_support
    plugins
    satpy_internals
    aux_data
    writing_tests
    testing

编码指南
========

Satpy 是 `Pytroll <http://pytroll.github.io/>`_ 的一部分，所有代码都应遵循 `Pytroll 编码指南和最佳实践 <http://pytroll.github.io/guidelines.html>`_。

Satpy 现在仅支持 Python 3，不再需要支持 Python 2。检查 ``pyproject.toml`` 以了解任何新代码需要支持的当前 Python 版本。

.. _devinstall:

开发安装
========

有关基本安装说明，请参阅 :doc:`../install` 部分。当需要安装 Satpy 时，应从 git 存储库的克隆中安装并以开发模式安装，以便本地文件更改自动反映在 python 环境中。我们强烈建议为开发创建一个单独的 conda 环境或 virtualenv。例如，您可以使用 conda_ 执行此操作::

  conda create -n satpy-dev python=3.11
  conda activate satpy-dev

然后从 git 存储库克隆并安装 Satpy::

  git clone https://github.com/pytroll/satpy.git
  cd satpy
  pip install -e .

这将以"可编辑"模式安装 Satpy，这意味着对源代码的任何更改都将立即在您的环境中可用。

.. note::

    有关开发 Satpy 的更多详细信息，请参阅完整的开发指南部分。
