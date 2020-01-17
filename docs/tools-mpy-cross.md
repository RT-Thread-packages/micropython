# 生成并运行 .mpy 文件

Python 工程中，.py 文件可以被编译成 .pyc 字节码文件。使用这类预先编译好的二进制文件的优势是一定程度上能够保护源代码，同时可以提高程序的加载速度。在 micropython 中同样地提供了类似的功能，能够将 .py 文件编译成 .mpy 文件，并且能够在MCU内直接运行，减少资源消耗的同时提高了程序的加载速度。本篇演示使用潘多拉开发板，以 hello world 工程为例，编译并运行该 demo 。

### 使用 mpy-cross 工具编译

RT-Thread 为开发者提供了便利的开发环境 ，针对 windows 平台提供了可以直接运行的 mpy-cross.exe ，无需拖带 Linux 环境，轻量且速度快。

本文将在 windows 环境中，使用软件包中提供的 mpy-cross.exe 软件。

在 RT-Thread/micropython 项目里找到 tools 文件夹，下载 mpy-cross.exe 。

这里以 `hellortt.py` 示例：

```python
class HelloRtt:
  def __repr__(self):
     self.__call__()
     return ""

  def __call__(self):
     print("hello world!!")
     print("hello RTT")

hello = HelloRtt()
```

首先将需要被编译的 `hellortt.py` 文件拖入到 mpy-cross.exe 所在文件夹中，在按住 shift 键的同时，点击鼠标右键，选择 `在此处打开 Powershell 窗口`（ cmd 窗口在这里也是可以使用的）。然后在 Powershell 中，键入 `.\mpy-cross.exe` 后面接上需要编译的工程 `hellortt.py` ：

![powershell_mpycross_deploy](assets/powershell_mpycross_deploy.PNG)

此时如果编译成功将会生成 mpy 文件，上图编译成功后，在文件夹中生成了 `hellortt.mpy` 文件。我们将 `hellortt.mpy` 拷贝到 MCU 的文件系统上，便可以像 .py 文件一样被 import 并调用。

### 拷贝至MCU文件系统中

将生成好的 .mpy 文件，拷贝至 MicroPython IDE 的工程中，并选中它，右键下载到开发板的文件系统中，如图：

![tools-mpy-download](assets/tools-mpy-download.png)

当下载完成之后，便可以在串口命令行中尝试 import 该 mpy 文件，执行该文件的函数，确认能够正常使用：

![mpy-usage-demo](assets/mpy-usage-demo.png)

如果运行时出现 `ValueError: invalid .mpy file` 错误，有可能是 MCU 上 的 micropython 固件与 mpy-cross 版本固件不相符所致，当前提供的 mpy-cross 工具支持 v1.12 版本的固件 。

