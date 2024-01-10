from setuptools import Extension, setup
from Cython.Build import cythonize

# from the command line at the project level type:
# > python setup.py build_ext --inplace
# to build the cython files to object files

extensions = [Extension(name='mylibrary',
                        sources=["mylibrary/**/*.pyx"],
                        extra_compile_args=['/O2'])]

setup(
    name='My Library',
    ext_modules=cythonize(extensions)
)
