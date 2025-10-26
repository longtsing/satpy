配置
====

Satpy 有两个级别的配置，可以控制 Satpy 及其各种组件的行为方式。有一系列"设置"可以更改全局 Satpy 行为。还有一系列"组件配置" YAML 文件，用于控制读取器、合成器、写入器和其他 Satpy 组件中的复杂功能，这些功能无法通过传统关键字参数控制。

设置
----

Satpy 中有一些配置参数不特定于某个组件，而是控制 Satpy 的更全局行为。这些参数可以通过以下三种方式之一设置：

1. 环境变量
2. YAML 文件
3. 在运行时使用 ``satpy.config``

此功能由 :doc:`donfig <donfig:configuration>` 库提供。下面描述了当前可用的设置。
每个选项都可以从所有三种方法中使用。如果指定为环境变量或在磁盘上的 YAML 文件中指定，则必须在导入 Satpy **之前**设置。

**YAML 配置**

包含这些参数的 YAML 文件可以位于以下任何位置：

1. ``<python environment prefix>/etc/satpy/satpy.yaml``
2. ``<user_config_dir>/satpy.yaml``（见下文）
3. ``~/.satpy/satpy.yaml``
4. ``<SATPY_CONFIG_PATH>/satpy.yaml``（见下面的 :ref:`config_path_setting`）

上述 ``user_config_dir`` 由 ``platformdirs`` 包提供，并因操作系统而异。典型的用户配置目录是：

* Mac OSX：``~/Library/Preferences/satpy``
* Unix/Linux：``~/.config/satpy``
* Windows：``C:\\Users\\<username>\\AppData\\Local\\pytroll\\satpy``

从上述路径找到的所有 YAML 文件将合并为一个配置对象（通过 ``satpy.config`` 访问）。
YAML 内容应该是配置键到其值的简单映射。例如：

.. code-block:: yaml

    cache_dir: "/tmp"
    data_dir: "/tmp"
    readers:
      clip_negative_radiances: True

请注意，点分隔的配置键（例如 ``readers.clip_negative_radiances``）应该在 ``satpy.yaml`` 中写成嵌套字典，如上例所示。
最后，可以通过设置环境变量 ``SATPY_CONFIG`` 来指定上述选项之外的其他配置路径。使用此环境变量指定的文件将在上述所有路径合并后最后添加。

**在运行时**

导入后，可以在运行时通过以下方式自定义值：

.. code-block:: python

    import satpy
    satpy.config.set(cache_dir="/my/new/cache/path")
    # ... 正常的 satpy 代码 ...

或者针对特定代码块：

.. code-block:: python

    import satpy
    with satpy.config.set(cache_dir="/my/new/cache/path"):
        # ... 一些 satpy 代码 ...
    # ... 使用原始 cache_dir 的代码

同样，如果您需要访问其中一个值，可以使用 ``satpy.config.get`` 方法。

缓存目录
^^^^^^^^

* **环境变量**：``SATPY_CACHE_DIR``
* **YAML/配置键**：``cache_dir``
* **默认值**：见下文

Satpy 缓存的任何文件将存储的目录。Satpy 不一定会清除此目录，但除非用户明确启用，否则很少使用。这默认为根据 `platformdirs <https://github.com/platformdirs/platformdirs#example-output>`_ "用户缓存目录"而不同的路径，具体取决于您的操作系统。

.. _config_cache_lonlats_setting:

缓存经度和纬度
^^^^^^^^^^^^^

* **环境变量**：``SATPY_CACHE_LONLATS``
* **YAML/配置键**：``cache_lonlats``
* **默认值**：``False``

是否应将生成的经度和纬度坐标缓存到磁盘上的 zarr 数组。目前这仅在非常特定的情况下有效。主要是在计算用于各种修饰符和合成器的传感器和太阳天顶角和方位角时生成的经度/纬度。此缓存仅针对基于 ``AreaDefinition`` 的地理定位完成，而不是针对 ``SwathDefinition``。数组存储在 ``cache_dir`` 中（见上文）。

将此设置为环境变量时，应使用 Python 布尔值的字符串等效项 ``="True"`` 或 ``="False"`` 进行设置。

另请参见下面的 ``cache_sensor_angles``。

.. warning::

    此缓存不限制条目数量，也不会使旧条目过期。由用户管理缓存目录的内容。

.. _config_cache_sensor_angles_setting:

缓存传感器角度
^^^^^^^^^^^^^

* **环境变量**：``SATPY_CACHE_SENSOR_ANGLES``
* **YAML/配置键**：``cache_sensor_angles``
* **默认值**：``False``

是否应将生成的传感器方位角和传感器天顶角缓存到磁盘上的 zarr 数组。这些角度主要用于某些修饰符和合成器。此缓存仅针对基于 ``AreaDefinition`` 的地理定位完成，而不是针对 ``SwathDefinition``。数组存储在 ``cache_dir`` 中（见上文）。

此缓存需要生成角度的估计值，以避免需要为每个新数据情况生成新角度。发生这种情况是因为角度生成取决于数据的观测时间和卫星的位置（经度、纬度、高度）。通过对所有情况使用恒定的观测时间（最大约 1e-10 误差）以及将卫星位置坐标四舍五入到最近的十分之一度（经度和纬度）和最近的十分之一米（最大约 0.058 误差）来估计角度。请注意，这些估计仅在启用缓存时完成（此参数为 True）。

将此设置为环境变量时，应使用 Python 布尔值的字符串等效项 ``="True"`` 或 ``="False"`` 进行设置。

另请参见上面的 ``cache_lonlats``。

.. warning::

    此缓存不限制条目数量，也不会使旧条目过期。由用户管理缓存目录的内容。

.. _config_path_setting:

组件配置路径
^^^^^^^^^^^

* **环境变量**：``SATPY_CONFIG_PATH``
* **YAML/配置键**：``config_path``
* **默认值**：``[]``

存储 Satpy 组件 YAML 配置文件的基本目录或多个目录。Satpy 期望特定组件类型的配置文件位于适当的子目录中（例如 ``readers``、``writers`` 等），但这些子目录不应包含在 ``config_path`` 中。
例如，如果您在 ``/my/config/dir/etc/composites/visir.yaml`` 中配置了自定义合成，则 ``config_path`` 应包含 ``/my/config/dir/etc``，以便 Satpy 在搜索合成时找到此配置文件。此选项取代了传统的 ``PPP_CONFIG_DIR`` 环境变量。

请注意，此值必须是列表。在 Python 中，可以通过以下方式设置：

.. code-block:: python

    satpy.config.set(config_path=['/path/custom1', '/path/custom2'])

如果设置环境变量，则在 Linux/OSX 上必须是冒号分隔（``:``）的字符串，或在 Windows 上是分号分隔（``;``）的字符串，并且必须在调用/导入 Satpy **之前**设置。如果环境变量是单个路径，则在导入 Satpy 时将其转换为列表。

.. code-block:: bash

    export SATPY_CONFIG_PATH="/path/custom1:/path/custom2"

在 Windows 上，使用 `C:` 驱动器上的路径，这些路径将是：

.. code-block:: bash

    set SATPY_CONFIG_PATH="C:/path/custom1;C:/path/custom2"

无论此设置如何，Satpy 将始终包含其分发的内置配置文件。当组件支持配置文件的合并时，它们以相反的顺序合并。这意味着"基本"配置路径应位于列表末尾，自定义/用户路径应位于列表开头。

.. _data_dir_setting:

数据目录
^^^^^^^^

* **环境变量**：``SATPY_DATA_DIR``
* **YAML/配置键**：``data_dir``
* **默认值**：见下文

Satpy 执行某些操作所需的任何数据将存储的目录。这取代了传统的 ``SATPY_ANCPATH`` 环境变量。这默认为根据 `platformdirs <https://github.com/platformdirs/platformdirs#example-output>`_ "用户数据目录"而不同的路径，具体取决于您的操作系统。

.. _download_aux_setting:

演示数据目录
^^^^^^^^^^^

* **环境变量**：``SATPY_DEMO_DATA_DIR``
* **YAML/配置键**：``demo_data_dir``
* **默认值**：<当前工作目录>

演示数据函数将数据文件下载到的目录。可用的演示数据函数可以在 :mod:`satpy.demo` 子包中找到。

下载辅助数据
^^^^^^^^^^^

* **环境变量**：``SATPY_DOWNLOAD_AUX``
* **YAML/配置键**：``download_aux``
* **默认值**：True

是否允许为某些 Satpy 操作下载辅助文件。有关更多信息，请参阅 :doc:`dev_guide/aux_data`。如果为 ``True``，则 Satpy 将在需要时下载并缓存任何必要的数据文件到 :ref:`data_dir_setting`。如果为 ``False``，则将使用预下载的文件，但不会下载或检查任何其他文件的有效性。

传感器角度位置偏好
^^^^^^^^^^^^^^^^^

* **环境变量**：``SATPY_SENSOR_ANGLES_POSITION_PREFERENCE``
* **YAML/配置键**：``sensor_angles_position_preference``
* **默认值**："actual"

控制在生成传感器方位角和传感器天顶角时应首选哪个卫星位置。此值直接传递给 :func:`~satpy.utils.get_satpos` 函数。有关如何使用该值的更多信息，请参阅该函数的文档。这用作 :func:`~satpy.modifiers.angles.get_angles` 和 :func:`~satpy.modifiers.angles.get_satellite_zenith_angle` 函数的一部分，这些函数被多个修饰符和合成器使用，包括默认的瑞利校正。

裁剪负红外辐射
^^^^^^^^^^^^^

* **环境变量**：``SATPY_READERS__CLIP_NEGATIVE_RADIANCES``
* **YAML/配置键**：``readers.clip_negative_radiances``
* **默认值**：False

是否在计算亮温之前将负红外辐射裁剪到最小允许值。
如果 ``clip_negative_radiances=False``，具有负辐射的像素将具有 ``np.nan`` 亮温。

负辐射裁剪目前已为以下读取器实现：

* ``abi_l1b``、``ami_l1b``、``fci_l1c_nc``

临时目录
^^^^^^^^

* **环境变量**：``SATPY_TMP_DIR``
* **YAML/配置键**：``tmp_dir``
* **默认值**：`tempfile.gettempdir()`_

Satpy 创建临时文件的目录，例如解压缩的输入文件。默认值取决于操作系统。

.. _tempfile.gettempdir(): https://docs.python.org/3/library/tempfile.html?highlight=gettempdir#tempfile.gettempdir


.. _component_configuration:

组件配置
--------

Satpy 的大部分功能来自它使用的各种组件，如读取器、写入器、合成器和增强。这些组件配置为从存储在 Satpy 内部或自定义用户配置文件中的 YAML 文件中重用。可以通过指定上面提到的 :ref:`config_path 设置 <config_path_setting>` 来提供自定义目录。

要创建和使用您自己的自定义组件配置，您应该：

1. 创建一个目录来存储您的新自定义 YAML 配置文件。每个组件的文件将放在特定于该组件的子目录中（例如 ``composites``、``enhancements``、``readers``、``writers``）。自定义 ``areas.yaml`` 也可以放在此目录的根目录中以配置区域定义。
2. 将 Satpy :ref:`config_path <config_path_setting>` 设置为指向您的新目录。这可以通过将环境变量 ``SATPY_CONFIG_PATH`` 设置为您的自定义目录（不要包含组件子目录）或设置此路径的其他方法之一来完成。
3. 使用您的自定义 YAML 文件创建 YAML 配置文件。在大多数情况下，无需从内置 Satpy 文件复制配置，因为这些文件将与您的自定义文件合并。
4. 如果您的自定义配置使用自定义 Python 代码，则此代码必须可由 Python 导入。这意味着您的代码必须安装在您的 Python 环境中，或者您必须将 ``PYTHONPATH`` 设置为模块的位置。
5. 运行您的 Satpy 代码，并像访问任何内置组件一样访问您的自定义组件。
