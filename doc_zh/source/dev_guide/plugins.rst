插件
====

Satpy 的插件系统允许扩展其功能而无需修改核心代码。

插件类型
========

Satpy 支持以下类型的插件：

* **读取器** - 用于读取新文件格式
* **写入器** - 用于写入新输出格式  
* **合成器** - 用于创建新的合成图像
* **修饰符** - 用于应用数据修改
* **增强** - 用于图像增强

创建插件
========

要创建 Satpy 插件：

1. 创建适当的 Python 类
2. 创建 YAML 配置文件
3. 将配置放在适当的目录中
4. 确保您的 Python 代码可导入

配置位置
========

插件配置应放在：

* ``$SATPY_CONFIG_PATH/readers/`` - 读取器
* ``$SATPY_CONFIG_PATH/writers/`` - 写入器
* ``$SATPY_CONFIG_PATH/composites/`` - 合成器和修饰符
* ``$SATPY_CONFIG_PATH/enhancements/`` - 增强

.. note::

    有关创建插件的详细说明，请参阅各个组件的文档。
