from setuptools import Extension, setup, find_packages
from Cython.Build import cythonize

# from the command line at the project level type:
# > python setup.py build_ext --inplace
# to build the cython files to object files

extensions = [Extension(name='mylibrary.mylibrary',
                        sources=['mylibrary/*.pyx'],
                        extra_compile_args=['/O2']),
              Extension(name='mylibrary.subdir.constants',
                        sources=['mylibrary/subdir/*.pyx'],
                        extra_compile_args=['/O2']),
              ]

cython_directives = {'embedsignature': True}

setup(
    name='mylibrary',
    version='0.0.0',  # todo: replace with meta data
    zip_safe=False,  # Without these two options
    include_package_data=True,  # PyInstaller may not find your C-Extensions
    ext_modules=cythonize(extensions, compiler_directives=cython_directives, language_level='3')
)
