# Project Template Documentation
## Initial Setup

* Download and install python 3.12.1 from https://www.python.org/downloads/
* Create a virtual environment.
* Install Kivy version 2.3.0: python -m pip install "kivy[full]"
* Install Cython 3.0.7: pip install cython 
* Download MSVC compiler, 2022 MSVC w/ C++ community edition.
- Got to: https://visualstudio.microsoft.com/vs/features/cplusplus/
  - Select Download Visual Studio with C++ 
  - Select Community edition, download and install. 
  - There is an option to download without the IDE:  https://visualstudio.microsoft.com/visual-cpp-build-tools/
  - Just for Reference, no action required: To determine the appropriate version of the C++ compiler: 
    - run: python -c "import sys; print(sys.version)"
    - The output will show the compiler version required: 
      - 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)]
      - See the table in the middle of the page: https://en.wikipedia.org/wiki/Microsoft_Visual_C%2B%2B 
This corresponds to runtime library version 14.37.32822
* Install Pyinstaller: pip install pyinstaller 
* Download and install Inno Setup: https://jrsoftware.org/isdl.php#stable

## To build the cython code
* From the project directory run:
```commandline
python setup.py build_ext --inplace
```

