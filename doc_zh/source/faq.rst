常见问题
========

以下是常见问题、性能提示和其他不太适合 Satpy 文档其余部分的主题。

如果您有此处未解答的任何其他问题，请随时在 GitHub 上创建问题或在 Slack 团队或邮件列表上与我们交谈。有关更多信息，请参阅 :ref:`贡献 <dev_help>` 文档。

.. contents:: 主题
    :depth: 1
    :local:


如何加速需要重采样的合成图像的创建？
------------------------------------

Satpy 会动态执行一些初始图像生成，但对于需要重采样的合成图像（如 GOES/ABI 的 ``true_color`` 合成图像），必须将数据重采样到公共网格，然后才能生成最终图像，因为输入通道具有不同的空间分辨率。在这种情况下，您可能会看到通过在加载合成图像时传递 ``generate=False`` 来获得显著的性能改进：

.. code-block:: python

    scn = Scene(filenames=filenames, reader='abi_l1b')
    scn.load(['true_color'], generate=False)
    scn_res = scn.resample(...)

默认情况下，``generate=True`` 意味着 Satpy 将使用可用数据创建尽可能多的合成图像。在某些情况下，这可能意味着许多中间产品（例如，使用为每个波段分辨率动态生成的角度的瑞利校正数据），然后需要重采样。
通过设置 ``generate=False``，Satpy 将仅从读取器加载必要的依赖项，但不会尝试生成任何合成图像或应用任何修饰符。在这些情况下，这可以节省大量时间和内存，因为只需处理一种分辨率的输入数据。请注意，当仅直接从读取器加载数据（例如，直接从文件加载红外/可见光波段）且不使用合成图像或修饰符时，此选项无效。另请注意，在大多数合成输入已经处于相同分辨率并且您仅生成有限数量的合成图像的情况下，``generate=False`` 实际上可能会损害性能。


为什么 Satpy 在我的强大机器上很慢？
------------------------------------

Satpy 在性能方面严重依赖 dask 库。然而，在某些系统上，dask 的默认设置实际上可能会损害性能。
默认情况下，dask 将为系统上的每个逻辑核心创建一个"工作器"。在大多数系统中，逻辑核心（也称为线程核心）的数量是物理核心的两倍。管理和与所有这些工作器通信可能会减慢 dask 的速度，特别是当大多数 Satpy 计算并未全部使用它们时。一个选项是通过在 python 代码的**顶部**执行以下操作来限制工作器的数量：

.. code-block:: python

    import dask
    dask.config.set(num_workers=8)
    # 所有其他 Satpy 导入和代码

这将限制 dask 使用 8 个工作器。通常 4 到 8 之间的数字是良好的起点。也可以在运行 python 脚本之前从环境变量设置工作器数量，因此无需修改代码：

.. code-block:: bash

    DASK_NUM_WORKERS=4 python myscript.py

同样，如果您有许多工作器处理大块数据，您可能使用的内存比预期的多得多。如果您限制工作器的数量*和*每个工作器处理的数据块的大小，您可以减少总体内存使用量。可以通过在代码周围使用以下内容在 Satpy 中配置默认块大小：

.. code-block:: python

    with dask.config.set("array.chunk-size": "32MiB"):
      # 你的代码在这里

有关 Satpy 中块大小的更多信息，请参阅 :doc:`overview` 中的 `数据块` 部分。

.. note::

    PYTROLL_CHUNK_SIZE 变量正在等待弃用，因此应该使用上述的 dask 配置参数。


为什么即使只有一个工作器也会使用多个 CPU？
-----------------------------------------

许多底层 Python 库使用用 C 或 FORTRAN 编写的数学库，如 BLAS 和 LAPACK，它们通常被编译为多线程。如果必要，可以通过设置环境变量强制线程数：

.. code-block:: bash

    OMP_NUM_THREADS=2 python myscript.py

工作器数量和线程数量之间有什么区别？
------------------------------------

上述问题处理并行化的两个不同阶段：Dask 工作器和数学库线程。

Dask 工作器的数量影响启动的单独任务数量，有效地告诉同时处理多少数据块。使用的工作器越多，内存使用量也越高。

线程数确定为每个工作器处理的块运行多少并行计算。这对内存使用的影响最小。

最优设置通常是这两个设置的混合，例如

.. code-block:: bash

    DASK_NUM_WORKERS=2 OMP_NUM_THREADS=4 python myscript.py

将创建两个工作器，每个工作器在调用底层数学库时将使用 4 个线程处理其数据块。

如何避免内存错误？
-----------------

如果您的环境使用许多 dask 工作器，它可能使用的内存超出必要。有关更改 Satpy 内存使用的更多信息，请参阅上面的"为什么 Satpy 在我的强大机器上很慢？"问题。

减少 GDAL 输出大小？
--------------------

有时基于 GDAL 的产品，如 geotiff，可能比预期的大得多。这可能是由 GDAL 的内部内存缓存与 dask 的数据数组分块冲突引起的。现代版本的 GDAL 默认使用 5% 的可用内存来保存数据，然后再压缩并写入磁盘。在更强大的系统（约 128GB 内存）上，这通常不是问题。然而，在低内存系统上，这可能意味着 GDAL 在写入磁盘之前只压缩少量数据。这导致压缩效果差，并且来自许多小压缩区域的开销很大。
一个解决方案是增加 dask 使用的块大小，但这可能导致计算期间性能不佳。另一个解决方案是增加 ``GDAL_CACHEMAX``，这是 GDAL 使用的环境变量。默认为 ``"5%"``，但可以增加::

    export GDAL_CACHEMAX="15%"

有关更多信息，请参阅 `GDAL 文档 <https://trac.osgeo.org/gdal/wiki/ConfigOptions#GDAL_CACHEMAX>`_。

写入 GeoTIFF 时如何使用多线程压缩？
-----------------------------------

GDAL 库的 GeoTIFF 驱动程序有许多选项可以更改 GeoTIFF 的格式和写入方式。在写入 GeoTIFF 时最重要的选项之一是使用多个线程来压缩数据。默认情况下，Satpy 将使用 DEFLATE 压缩，它的压缩速度可能比其他选项慢，但读取速度更快。GDAL 允许我们通过指定 ``num_threads`` 选项来控制压缩期间使用的线程数。此选项默认为 ``1``，但建议将其设置为至少与您使用的 dask 工作器数量相同。通过向 `save_dataset` 或 `save_datasets` 调用添加 ``num_threads`` 来执行此操作::

    scn.save_datasets(base_dir='/tmp', num_threads=8)

Satpy 还将我们的数据存储为"tiles"而不是"stripes"，这是更有效地压缩 GeoTIFF 图像的另一种方法。您可以使用 ``tiled=False`` 禁用此功能。

有关可用的创建选项（包括其他压缩选择）的更多信息，请参阅 `GDAL GeoTIFF 文档 <https://gdal.org/drivers/raster/gtiff.html#creation-options>`_。

为什么 matplotlib 在使用 ``pyplot.imshow`` 时返回错误 ``Invalid shape (3, Ny, Nx) for image data``？
-----------------------------------------------------------------------------------------------

Satpy 数据集在内存中存储时，波段维度在前，然后是垂直和水平空间索引，而 matplotlib 期望形状为 ``(M, N, 3)``（RGB）或 ``(M, N, 4)``（RGBA）的数组。

Satpy 的数据集可以通过增强转换为适当的值范围，因此例如，要显示 ``natural_color`` 合成图像，假设场景加载在变量 ``scn`` 中，可以使用以下代码。

.. code-block:: python

   from satpy.writers import get_enhanced_image

   im = get_enhanced_image(scn['natural_color'])
   im.data.plot.imshow(rgb='bands')

在这里，实用程序 :func:`~xarray.plot.imshow` 将为 matplotlib 的例程准备数据。可以按如下方式获得类似的结果：

.. code-block:: python

    plt.imshow((sub_scn['natural_color'].transpose('y', 'x', 'bands') / 100 * 255).astype('uint8'))

要了解更多关于 Satpy 如何为图像缩放数据以及有关 :func:`~satpy.enhancements.enhancer.get_enhanced_image` 函数的更多信息，请参阅 :doc:`enhancements` 文档。
