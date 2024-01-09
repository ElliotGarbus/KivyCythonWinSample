from setuptools import setup
from Cython.Build import cythonize

setup(
    name='My Library',
    ext_modules=cythonize("mylibrary/**/*.pyx"),
)
