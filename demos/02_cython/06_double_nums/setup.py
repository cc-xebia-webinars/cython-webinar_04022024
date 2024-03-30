from setuptools import setup
from Cython.Build import cythonize

setup(ext_modules=cythonize("double_nums_mod.pyx"))
