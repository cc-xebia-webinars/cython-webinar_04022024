from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    name="mandelbrot",
    ext_modules=cythonize("mandelbrot.pyx"),
    include_dirs=[numpy.get_include()],
)
