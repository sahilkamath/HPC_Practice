from Cython.Build import cythonize
from setuptools import setup

setup(ext_modules=cythonize("cython_harmonic_series.pyx"))
