from setuptools import find_packages, setup


def read(filename):
    with open(filename) as file:
        return file.read()


setup(
    name='rawg',
    version='1.0.1',
    author='uburuntu',
    author_email='bekbulatov.ramzan@ya.ru',
    url='https://github.com/uburuntu/rawg',
    description='RAWG.io API Wrapper',
    long_description=read('readme.md'),
    long_description_content_type="text/markdown",
    download_url='https://github.com/uburuntu/rawg/archive/master.zip',
    packages=find_packages(exclude=["test", "tests"]),
    requires_python='>=3.6',
    install_requires=['urllib3 >= 1.15', 'six >= 1.10', 'certifi', 'python-dateutil', 'aiohttp >= 3.0.0'],
    keywords=['RAWG Video Games Database API', 'OpenAPI'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
    ],
)
