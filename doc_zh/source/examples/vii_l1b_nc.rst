EPS-SG VII netCDF 示例
======================

Satpy 包含 EPS-SG 可见光和红外成像仪（VII）1b 级数据的读取器。以下 Python 代码片段展示了如何使用 Satpy 读取通道、重采样并将图像保存到欧洲区域的示例。

.. warning::

    此示例目前正在进行中。下面的某些代码可能无法与当前发布的 Satpy 版本一起使用。此示例的其他更新将很快推出。

.. code-block:: python

    import glob
    from satpy.scene import Scene

    # 查找要读取的文件
    filenames = glob.glob('/path/to/VII/data/W_xx-eumetsat-darmstadt,SAT,SGA1-VII-1B-RAD_C_EUMT_20191007055100*')

    # 从选定的粒度创建 VII 场景
    scn = Scene(filenames=filenames, reader='vii_l1b_nc')

    # 打印此场景的可用数据集名称
    print(scn.available_dataset_names())

    # 加载感兴趣的数据集
    # 注意：测试数据仅支持辐射
    scn.load(["vii_668"], calibration="radiance")

    # 将场景重采样到指定区域（例如，欧洲 1km 分辨率的 "eurol1"）
    eur = scn.resample("eurol", resampler='nearest', radius_of_influence=5000)

    # 将重采样的数据保存到磁盘
    eur.save_dataset("vii_668", filename='./vii_668_eur.png')
