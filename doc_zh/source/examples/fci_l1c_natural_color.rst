MTG FCI - 自然彩色示例
=======================

Satpy 包含 Meteosat 第三代（MTG）FCI 1c 级数据的读取器。以下 Python 代码片段展示了如何使用 Satpy 在欧洲区域生成自然彩色 RGB 合成图像的示例。

.. warning::

    此示例目前正在进行中。下面的某些代码可能无法与当前发布的 Satpy 版本一起使用。此示例的其他更新将很快推出。

.. note::

    要读取压缩数据，需要解压缩库。安装 FCIDECOMP 库（请参阅 `FCI L1 产品用户指南 <https://www.eumetsat.int/media/45923>`_），或使用以下命令安装 ``hdf5plugin`` 包::

        pip install hdf5plugin

    或::

        conda install hdf5plugin -c conda-forge

    如果您使用 ``hdf5plugin``，请确保在脚本顶部添加 ``import hdf5plugin`` 行。

.. code-block:: python

    from satpy.scene import Scene
    from satpy import find_files_and_readers

    # 定义 FCI 测试数据文件夹的路径
    path_to_data = 'your/path/to/FCI/data/folder/'

    # 查找文件并分配 FCI 读取器
    files = find_files_and_readers(base_dir=path_to_data, reader='fci_l1c_nc')

    # 从选定的文件创建 FCI 场景
    scn = Scene(filenames=files)

    # 打印此场景的可用数据集名称（例如 'vis_04'、'vis_05'、'ir_38',...）
    print(scn.available_dataset_names())

    # 打印此场景的可用合成名称（例如 'natural_color'、'airmass'、'convection',...）
    print(scn.available_composite_names())

    # 加载感兴趣的数据集/合成
    scn.load(['natural_color'])

    # 将场景重采样到指定区域（例如欧洲区域）
    scn_resampled = scn.resample('eurol1')

    # 将重采样的数据保存到磁盘
    scn_resampled.save_dataset('natural_color', filename='./fci_natural_color_eur.png')
