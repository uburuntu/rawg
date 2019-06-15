import setuptools

import rawg


def read(filename):
    with open(filename) as file:
        return file.read()


setuptools.setup(
    name='rawg',
    version=rawg.__version__,
    author='uburuntu',
    author_email='bekbulatov.ramzan@ya.ru',
    url='https://github.com/uburuntu/rawg',
    description='RAWG.io API Wrapper',
    long_description=read('readme.md'),
    long_description_content_type="text/markdown",
    download_url='https://github.com/uburuntu/rawg/archive/master.zip',
    packages=['rawg'],
    requires_python='>=3.6',
    install_requires=['aiohttp', 'pydantic', 'requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
    ],
)
