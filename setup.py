import os
import re
from setuptools import find_packages, setup

def get_version():
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)
    
with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='transform3d',
    version='0.1',
    url='https://github.com/LeOntalEs/transform3d',
    packages=find_packages(),
    include_package_data=True,
    license='MIT License',
    description='transformation 2D image in 3D space work with python-opencv',
    long_description=README,
    author='Taratep Sira-aksorn',
    author_email='taratep.sira@gmail.com',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)