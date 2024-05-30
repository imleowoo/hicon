from pathlib import Path

from setuptools import setup, find_packages

install_requires = [
    "gne",
    "pyppeteer",
]
test_requires = [
    "pytest>=3",
]

version = (Path(__file__).parent / 'hicon' / 'VERSION').read_text('ascii').strip()

setup(
    name='hicon',
    version=version,
    description='HiContent 一个正文提取工具',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    # The project URL
    url='https://git.umlife.net/mt-data/open-data',

    # Author
    author='youmi',
    maintainer='Leo',
    maintainer_email='wulei@youmi.com',

    # license
    license='MIT',

    entry_points={
        'console_scripts': [
            'hicon = hicon.main:cli',  # 注册命令
        ],
    },

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11'
    ],
    packages=find_packages(
        include=['hicon'],
    ),
    include_package_data=True,
    install_requires=install_requires,
    tests_require=test_requires,
    python_requires='>=3.8',
    project_urls={
        'Source': 'https://git.umlife.net/mt-data/open-data',
    },
)
