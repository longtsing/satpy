MultiScene（实验性）
===================

Satpy 中的 Scene 对象旨在表示特定时刻或时间范围内的单个地理区域。这意味着它们不适合处理极地轨道卫星数据的多个轨道、地球静止卫星数据的多个时间步长或其他特殊数据情况。为了处理这些情况，Satpy 提供了 `MultiScene` 类。以下示例将介绍 MultiScene 的一些基本用例。

.. warning::

    这些功能仍处于早期开发阶段，随着收到更多用户反馈和添加更多功能，可能会随时间而变化。

创建 MultiScene
----------------
有两种方法可以创建 ``MultiScene``。一种是手动创建并提供场景对象，

    >>> from satpy import Scene, MultiScene
    >>> from glob import glob
    >>> scenes = [
    ...    Scene(reader='viirs_sdr', filenames=glob('/data/viirs/day_1/*t180*.h5')),
    ...    Scene(reader='viirs_sdr', filenames=glob('/data/viirs/day_2/*t180*.h5'))
    ... ]
    >>> mscn = MultiScene(scenes)
    >>> mscn.load(['I04'])

或者使用 :meth:`MultiScene.from_files <satpy.multiscene._multiscene.MultiScene.from_files>` 类方法从一系列文件创建 ``MultiScene``。这使用 :func:`~satpy.readers.core.grouping.group_files` 实用函数按开始时间或其他文件名参数对文件进行分组。

   >>> from satpy import MultiScene
   >>> from glob import glob
   >>> mscn = MultiScene.from_files(glob('/data/abi/day_1/*C0[12]*.nc'), reader='abi_l1b')
   >>> mscn.load(['C01', 'C02'])

.. versionadded:: 0.12

    ``from_files`` 和 ``group_files`` 函数在 Satpy 0.12 中添加。有关替代解决方案，请参见下文。

对于旧版本的 Satpy，我们可以手动创建使用的 `Scene` 对象。使用 :func:`~glob.glob` 函数和 for 循环将文件分组到 Scene 对象中，如果单独使用，可以加载我们想要的数据。下面的代码等同于上面的 ``from_files`` 代码：

    >>> from satpy import Scene, MultiScene
    >>> from glob import glob
    >>> scenes = []
    >>> for files in [glob('/data/abi/day_1/*C0[12]*.nc')]:
    ...     scenes.append(Scene(reader='abi_l1b', filenames=files))
    >>> mscn = MultiScene(scenes)
    >>> mscn.load(['C01', 'C02'])

.. note::

    有关 MultiScene 功能的更多详细信息和高级用法，请参阅 API 文档。
