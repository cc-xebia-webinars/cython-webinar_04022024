from setuptools import setup
from Cython.Build import cythonize

# cythonize - A function that accepts a list of source files and compiles them
# to C and then returns list of Extension objects.

# setup - A function that accepts a list of Extension objects and compiles them
# to shared libraries.

setup(ext_modules=cythonize("./utils/utils.pyx"))
