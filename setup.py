from setuptools import setup
from Cython.Build import cythonize

# from the command line at the project level type:
# > python setup.py build_ext --inplace
# to build the cython files to object files

setup(
    name='My Library',
    ext_modules=cythonize("mylibrary/**/*.pyx"),
)
