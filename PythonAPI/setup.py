from setuptools import setup, Extension
import numpy as np

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'excocotools._mask',
        sources=['../common/maskApi.c', 'excocotools/_mask.pyx'],
        include_dirs = [np.get_include(), '../common'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='excocotools',
    packages=['excocotools'],
    package_dir = {'excocotools': 'excocotools'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='1.0',
    description="Extended COCO API",
    url="https://github.com/jin-s13/excocoapi",
    ext_modules= ext_modules
)
