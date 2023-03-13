import os
from importlib.machinery import SourceFileLoader

from pkg_resources import parse_requirements
from setuptools import find_packages, setup

module_name = 'flashlight'

module = SourceFileLoader(
    module_name, os.path.join(module_name, '__init__.py')
).load_module()


def load_requirements(fname: str) -> list:
    requirements = []
    with open(fname, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


requirements_txt = 'requirements.txt'


setup(
    name=module_name,
    version=module.__version__,
    author=module.__author__,
    author_email=module.__email__,
    license=module.__license__,
    description=module.__doc__,
    url='https://github.com/hotaged/ligth',
    platforms='all',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: Russian',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: CPython'
    ],
    python_requires='<3.10',
    packages=find_packages(exclude=['tests', 'mock-flashlight-server', 'database']),
    install_requires=load_requirements('requirements.txt'),
    entry_points={
        'console_scripts': [
            f'{module_name} = {module_name}.__main__:cli'
        ]
    },
    include_package_data=True
)
