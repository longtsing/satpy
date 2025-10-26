编写测试
========

为 Satpy 贡献代码时，编写测试非常重要。

测试框架
========

Satpy 使用 pytest 作为测试框架。

测试类型
========

单元测试
--------

测试单个函数或方法的行为。

集成测试
--------

测试多个组件如何协同工作。

编写测试的最佳实践
==================

1. **隔离测试** - 每个测试应该独立
2. **使用 fixtures** - 共享测试设置
3. **模拟外部依赖** - 使用 mock 对象
4. **测试边界情况** - 包括错误情况
5. **保持测试简单** - 一个测试一个概念

示例
====

.. code-block:: python

    import pytest
    from satpy import Scene

    def test_scene_creation():
        """测试创建空场景"""
        scn = Scene()
        assert len(scn) == 0

    def test_scene_load(tmp_path):
        """测试加载数据"""
        # 测试实现

运行测试
========

要运行所有测试：

.. code-block:: bash

    pytest

要运行特定测试文件：

.. code-block:: bash

    pytest satpy/tests/test_scene.py

.. note::

    有关测试的更多详细信息，请参阅完整的测试文档。
