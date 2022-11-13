from pkg_resources import parse_requirements
from setuptools import find_packages, setup


def read(filename):
    with open(filename) as file:
        return file.read()


def load_requirements(filename: str) -> list:
    requirements = []
    for req in parse_requirements(read(filename)):
        extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
        requirements.append(
            '{}{}{}'.format(req.name, extras, req.specifier)
        )
    return requirements


setup(
    name='rawg',
    version='1.2.0',
    author='uburuntu',
    author_email='bekbulatov.ramzan@ya.ru',
    url='https://github.com/uburuntu/rawg',
    description='RAWG.io API Wrapper',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    download_url='https://github.com/uburuntu/rawg/archive/master.zip',
    packages=find_packages(exclude=["test", "tests"]),
    requires_python='>=3.6',
    install_requires=load_requirements('requirements.txt'),
    extras_require={'test': load_requirements('test-requirements.txt')},
    keywords=['RAWG Video Games Database API', 'OpenAPI'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Programming Language :: Python :: 3',
    ],
)
