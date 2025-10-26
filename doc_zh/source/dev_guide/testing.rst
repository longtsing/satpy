测试
====

本文档描述了如何运行 Satpy 的测试套件。

先决条件
========

要运行测试，您需要安装：

* pytest
* pytest-cov（用于覆盖率报告）
* 其他测试依赖项（参见 pyproject.toml）

运行测试
========

运行所有测试
------------

.. code-block:: bash

    pytest

运行特定模块的测试
------------------

.. code-block:: bash

    pytest satpy/tests/reader_tests/

生成覆盖率报告
--------------

.. code-block:: bash

    pytest --cov=satpy --cov-report=html

持续集成
========

Satpy 使用 GitHub Actions 进行持续集成。每个拉取请求都会自动运行测试。

.. note::

    确保在提交拉取请求之前所有测试都通过。
