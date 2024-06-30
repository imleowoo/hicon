# Hi Content

一个通过URL提取正文的工具

# Python Package 造轮子分享文档

## Package 的主流安装工具 PIP

### 什么是pip？

Package Installer for Python 的缩写

PYPI主页：https://pypi.org/project/pip/

官方主页：https://pip.pypa.io/en/stable/installation/#python

### 如何获取pip？

1. 通常在官网下载的Python ≥ 3.4 的版本自带了pip
2. 虚拟环境中创建的Python环境会自带pip
3. 使用Python自带的`ensurepip`模块来启用安装pip

   [ensurepip --- 初始设置 pip 安装器](https://docs.python.org/zh-cn/3/library/ensurepip.html#module-ensurepip)

    ```bash
    (pypkg) ➜  ~ python -m ensurepip
    Looking in links: /var/folders/d_/y10kxt7j14s3ryj8966pkznw0000gn/T/tmplw17z50q
    Requirement already satisfied: setuptools in ./.pyenv/versions/3.10.9/envs/pypkg/lib/python3.10/site-packages (65.5.0)
    Requirement already satisfied: pip in ./.pyenv/versions/3.10.9/envs/pypkg/lib/python3.10/site-packages (22.3.1)
    ```

4. 使用pip官方的 [get-pip.py](https://bootstrap.pypa.io/get-pip.py) 来安装
5. 以前在Linux中直接使用`apt install python3`，得到的Python可能是不带pip的

### 如何使用pip？

#### 安装Package

1. 直接指定包名安装

    ```bash
    $ python -m pip <pip arguments>

    python -m pip install SomePackage            # latest version
    python -m pip install SomePackage==1.0.4     # specific version
    python -m pip install 'SomePackage>=1.0.4'     # minimum version

    ```

2. 使用 `-r` 读取 `requirements` 文件安装

   批量安装项目环境依赖

    ```bash
    python -m pip install -r requirements.txt
    ```

3. 从轮子wheel文件 `.whl` 安装

   通常各类Python软件源里面都会有编译过的`wheel`文件

   在清华源的以`Scrapy`为例：https://pypi.tuna.tsinghua.edu.cn/simple/scrapy/

    ```bash
    python -m pip install SomePackage-1.0-py2.py3-none-any.whl
    ```

   **特点：**

    1. **安装速度快**：安装时候不需要编译源代码
    2. **兼容性好和减少编译错误**：编译源代码包时可能会遇到各种编译错误，尤其是在不同的操作系统或具有不同配置的系统上。比如以前Windows有些依赖装不上。
    3. **私有构建打包成whl：**离线安装、项目封装等

    ```bash
    # 自行构建 *.whl 文件
    # 默认输出 whl 至 /dist 文件夹下
    $ python setup.py bdist_wheel
    ```

4. 使用发行的压缩包安装

   可以完成 下载→解压→安装 的操作

   以 **scrapy** 为例：https://github.com/scrapy/scrapy/releases

    ```bash
    # 直接通过 tar.gz 文件安装
    pip install scrapy-2.11.2.tar.gz

    # 或者通过 tar.gz 文件URL安装
    # pip install https://github.com/psf/requests/releases/download/v2.32.3/requests-2.32.3.tar.gz
    pip install https://github.com/scrapy/scrapy/archive/refs/tags/2.11.2.tar.gz

    # ----------
    Processing /Users/leiwu/Downloads/scrapy-2.11.2.tar.gz
      Preparing metadata (setup.py) ... done
    Requirement already satisfied: Twisted>=18.9.0 in /Users/leiwu/.pyenv/versions/3.10.9/envs/pypkg/lib/python3.10/site-packages (from Scrapy==2.11.2) (24.3.0)
    Collecting cryptography>=36.0.0
      Using cached cryptography-42.0.7-cp39-abi3-macosx_10_12_universal2.whl (5.9 MB)
    Requirement already satisfied: cssselect>=0.9.1 in /Users/leiwu/.pyenv/versions/3.10.9/envs/pypkg/lib/python3.10/site-packages (from Scrapy==2.11.2) (1.2.0)
    Collecting itemloaders...
    ```

5. 通过仓库 repository 安装

    ```bash
    # 直接通过项目仓库安装
    pip install git+https://github.com/scrapy/scrapy.git

    # -----
    Collecting git+https://github.com/scrapy/scrapy.git
      Cloning https://github.com/scrapy/scrapy.git to /private/var/folders/d_/y10kxt7j14s3ryj8966pkznw0000gn/T/pip-req-build-hjvw1m6y
      Running command git clone --filter=blob:none --quiet https://github.com/scrapy/scrapy.git /private/var/folders/d_/y10kxt7j14s3ryj8966pkznw0000gn/T/pip-req-build-hjvw1m6y
      Resolved https://github.com/scrapy/scrapy.git to commit 1282ddf8f77299edf613679c2ee0b606e96808ce
      Preparing metadata (setup.py) ... done
    Collecting Twisted>=18.9.0
    ```

6. 通过源码安装

    ```bash
    # 进入源码路径
    $ cd scrapy
    # 执行安装
    $ pip install .
    # 等同于
    $ python setup.py install

    # --------
    Processing /Users/leiwu/Projects/scrapy
      Preparing metadata (setup.py) ... done
    Requirement already satisfied: Twisted>=18.9.0 in /Users/leiwu/.pyenv/versions/3.10.9/envs/pypkg/lib/python3.10/site-packages (from Scrapy==2.11.2) (24.3.0)
    Collecting cryptography>=36.0.0
      Using cached cryptography-42.0.7-cp39-abi3-macosx_10_12_universal2.whl (5.9 MB)
    ....
    ```

#### 完整PIP命令

```bash
pip install --help

Usage:
  pip install [options] <requirement specifier> [package-index-options] ...
  pip install [options] -r <requirements file> [package-index-options] ...
  pip install [options] [-e] <vcs project url> ...
  pip install [options] [-e] <local project path> ...
  pip install [options] <archive url/path> ...

Description:
  Install packages from:

  - PyPI (and other indexes) using requirement specifiers.
  - VCS project urls.
  - Local project directories.
  - Local or remote source archives.

  pip also supports installing from "requirements files", which provide
  an easy way to specify a whole environment to be installed.
```

```bash
$ pip help

Usage:
  pip <command> [options]

Commands:
  install                     Install packages.
  download                    Download packages.
  uninstall                   Uninstall packages.
  freeze                      Output installed packages in requirements format.
  inspect                     Inspect the python environment.
  list                        List installed packages.
  show                        Show information about installed packages.
  check                       Verify installed packages have compatible dependencies.
  config                      Manage local and global configuration.
  search                      Search PyPI for packages.
  cache                       Inspect and manage pip's wheel cache.
  index                       Inspect information available from package indexes.
  wheel                       Build wheels from your requirements.
  hash                        Compute hashes of package archives.
  completion                  A helper command used for command completion.
  debug                       Show information useful for debugging.
  help                        Show help for commands.
```

# **setup.py** 是什么

[Packaging and distributing projects - Python Packaging User Guide](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)

1. 这是配置项目各个方面的文件。`setup.py`的主要功能是它包含全局`setup()`函数。该函数的关键字参数是如何定义项目的具体细节。最相关的论点将在下面的部分中解释。
2. 它是用于运行与打包任务相关的各种命令的命令行界面。要获取可用命令的列表，请运行`python3 setup.py --help-commands`

[以scrapy项目的setup.py](http://以scrapy项目的setup.py) 为例

https://github.com/scrapy/scrapy/blob/master/setup.py

## 开发一个正文提取工具`hicon`

`hicon = Hi Content`

可以将新闻、文章这类站点，访问URL即可将其文章标题、正文、作者、发布日期 提取出来。

### 运行效果

1. 可安装后导包使用

    ```python
    import asyncio

    from hicon import extract

    async def run():
        result = await extract('https://news.ifeng.com/c/8a0ytPBvYg6')
        print(result)

    if __name__ == '__main__':
        asyncio.run(run())

    # 输出结果
    {'title': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修', 'author': '', 'publish_time': '2024-05-31 22:18:41', 'content': '圆明园 视觉中国 资料图\n北京晚报微信公号5月30日消息，一场疾风迅雨后，圆明园内的树木倒伏不少，因为要清理树木，5月31日闭园一天。\n通过游人拍摄的照片和视频可以看出，圆明园内有大量树木倒伏，在主干道两侧，可见一些大树横七竖八地躺在地上，有的被连根拔起，裸露出盘根错节的根系；有的树杈被折断，甚至整个树冠都断裂了，凌乱的枝叶也散落一地。湖畔的大树也倒伏了不少，树冠连着树干直接倒在了水里。还有大树砸在了屋顶上。\n记者从圆明园获悉，因为这场区域性暴雨大风天气，圆明园内约有逾百棵树木倒伏，阻碍了园内多条道路，存在一定隐患，景区立即采取相关措施，清理倒伏树木、抢修相关路段，游客只出不进。为确保游客安全，5月31日，圆明园拟采取闭园措施，继续开展清理树木、路面抢修等相关工作。', 'images': ['//d.ifengimg.com/w1035_h582_q90_webp/x0.ifengimg.com/res/2024/F5EC158CB60AC7B87F5C7A415F6A7118F3C2FB0F_size126_w1035_h582.jpg', 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEXy8vJkA4prAAAACklEQVQI12NgAAAAAgAB4iG8MwAAAABJRU5ErkJggg=='], 'meta': {'referrer': 'always', 'keywords': '圆明园 树木 闭园 大树 根系 资料 游人 中国 疾风 树干 消息 树冠 措施 北京 隐患 暴雨 天气 大风 照片 屋顶 北京晚报 盘根错节 视觉 景区 树杈 区域性 路段 视频 记者 公号 日闭园 横七竖八 湖畔 道路 大量 游客 路面 主干道', 'description': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修', 'og: webtype': 'news', 'og:url': 'https://news.ifeng.com/c/8a0ytPBvYg6', 'og:title': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修', 'og:description': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修', 'og:time ': '2024-05-31 22:18:41', 'og:category ': '凤凰网资讯', 'og:image': 'https://x0.ifengimg.com/ucms/2024_22/998FC35DF8EB446F3187047748289881D04B1284_size183_w975_h549.jpg', 'og:img_slide': '', 'og:img_video': ''}}
    ```

2. 支持命令行调用

    ```bash
    $ hicon https://news.ifeng.com/c/8a0ytPBvYg6

    # -----
    {'author': '',
     'content': '圆明园 视觉中国 资料图\n'
                '北京晚报微信公号5月30日消息，一场疾风迅雨后，圆明园内的树木倒伏不少，因为要清理树木，5月31日闭园一天。\n'
                '通过游人拍摄的照片和视频可以看出，圆明园内有大量树木倒伏，在主干道两侧，可见一些大树横七竖八地躺在地上，有的被连根拔起，裸露出盘根错节的根系；有的树杈被折断，甚至整个树冠都断裂了，凌乱的枝叶也散落一地。湖畔的大树也倒伏了不少，树冠连着树干直接倒在了水里。还有大树砸在了屋顶上。\n'
                '记者从圆明园获悉，因为这场区域性暴雨大风天气，圆明园内约有逾百棵树木倒伏，阻碍了园内多条道路，存在一定隐患，景区立即采取相关措施，清理倒伏树木、抢修相关路段，游客只出不进。为确保游客安全，5月树木、路面抢修等相关工作。',
     'images': ['//d.ifengimg.com/w1035_h582_q90_webp/x0.ifengimg.com/res/2024/F5EC158CB60AC7B87F5C7A415F6A7118F3C2FB0F_size126_w1035_h582.jpg',
                'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEXy8vJkA4prAAAACklEQVQI12NgAAAAAgAB4iG8MwAAAABJRU5ErkJggg=='],
     'meta': {'description': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修',
              'keywords': '圆明园 树木 闭园 大树 根系 资料 游人 中国 疾风 树干 消息 树冠 措施 北京 隐患 暴雨 天气 大风 '
                          '照片 屋顶 北京晚报 盘根错节 视觉 景区 树杈 区域性 路段 视频 记者 公号 日闭园 横七竖八 湖畔 道路 '
                          '大量 游客 路面 主干道',
              'og: webtype': 'news',
              'og:category ': '凤凰网资讯',
              'og:description': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修',
              'og:image': 'https://x0.ifengimg.com/ucms/2024_22/998FC35DF8EB446F3187047748289881D04B1284_size183_w975_h549.jpg',
              'og:img_slide': '',
              'og:img_video': '',
              'og:time ': '2024-05-31 22:18:41',
              'og:title': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修',
              'og:url': 'https://news.ifeng.com/c/8a0ytPBvYg6',
              'referrer': 'always'},
     'publish_time': '2024-05-31 22:18:41',
     'title': '北京圆明园内逾百棵树木倒伏，明日闭园清理抢修'}


     $ which hicon
     /Users/leiwu/.pyenv/versions/3.10.9/envs/hicon/bin/hicon
    ```

### 创建项目

```bash
$ tree -L 1
.
├── LICENSE # 许可
├── MANIFEST.in # 用于指定需要包含的非py文件
├── README.md # README
├── hicon # 源码目录
├── setup.py # 安装配置
└── tests # 测试用例
```

必要的文件

1. `hicon` 工具源代码目录
2. [`setup.py](http://setup.py)` 安装配置文件

### 项目开发

略

### 更新至**`pyproject.toml`**

安装部分package时会出现告警：

```bash
DEPRECATION: gne is being installed using the legacy 'setup.py install' method, because it does not have a 'pyproject.toml' and the 'wheel' package is not installed. pip 23.1 will enforce this behaviour change. A possible replacement is to enable the '--use-pep517' option. Discussion can be found at https://github.com/pypa/pip/issues/8559
```

`pyproject.toml`是打包工具以及其他工具（例如 linter、类型检查器等）使用的配置文件。此文件中存在三个可能的 TOML 表

TOML 通常用于配置文件

`pyproject.toml`

1. 打包工具的配置项
2. 其他工具（例如 linter、类型检查器等）

#### 以 [fastapi](https://github.com/tiangolo/fastapi/blob/master/pyproject.toml) 项目为例

https://github.com/tiangolo/fastapi/blob/master/pyproject.toml

通常有这三个配置项类别

1. `[build-system]`
    1. 声明您使用哪个构建后端以及构建项目所需的其他依赖项

    ```toml
    [build-system]
    requires = ["setuptools >= 61.0"]
    build-backend = "setuptools.build_meta"
    ```

2. `[project]`
    1. 构建后端用来指定项目基本元数据的格式，例如依赖项、您的姓名等，与`setup()` 参数类似
3. `[tool]`
    1. `[tool.isort]`
    2. `[tool.black]`

## 其它

1. 项目布局 `*src-layout`、`flat-layout` 、`single-module`*
    - setuptools.discovery

        ```python
        """Automatic discovery of Python modules and packages (for inclusion in the
        distribution) and other config values.

        For the purposes of this module, the following nomenclature is used:

        # requests
        - "src-layout": a directory representing a Python project that contains a "src"
          folder. Everything under the "src" folder is meant to be included in the
          distribution when packaging the project. Example::

            .
            ├── tox.ini
            ├── pyproject.toml
            └── src/
                └── mypkg/
                    ├── __init__.py
                    ├── mymodule.py
                    └── my_data_file.txt

        # scrapy/fastapi/hicon
        - "flat-layout": a Python project that does not use "src-layout" but instead
          have a directory under the project root for each package::

            .
            ├── tox.ini
            ├── pyproject.toml
            └── mypkg/
                ├── __init__.py
                ├── mymodule.py
                └── my_data_file.txt

        # bottle
        - "single-module": a project that contains a single Python script direct under
          the project root (no directory used)::

            .
            ├── tox.ini
            ├── pyproject.toml
            └── mymodule.py

        """
        ```

2. requirements 和 setup.py 的区别？
    1. `requirements.txt` 文件列出了项目运行所需的所有依赖项，通常每行一个依赖，并且可以指定版本号。这种方式简洁明了，易于阅读和使用
    2. `setup.py` 文件是一个构建和安装脚本，用于定义项目的元数据和依赖关系。它使用`setuptools`库，可以执行包的构建、安装、分发等操作。
    3. `requirements.txt`更侧重于快速列出依赖项，而`setup.py`提供了更全面的包管理和分发功能
3. pyproject.toml 又是什么？

   https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

## 参考

1. [**Packaging and distributing projects
   **](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)
2. [**`ensurepip`--- 初始设置 pip 安装器**](https://docs.python.org/zh-cn/3/library/ensurepip.html#module-ensurepip)
3. [**unittest --- Unit testing framework**](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
4. [**src layout vs flat layout**](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
