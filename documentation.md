# Project Template Documentation
## Initial Setup

* Download and install python 3.12.1 from https://www.python.org/downloads/
* Create a virtual environment.
* Install Kivy version 2.3.0: python -m pip install "kivy[full]"
* Install Cython 3.0.7: pip install cython
* Install pywin32: pip install pywin32
* Download MSVC compiler, 2022 MSVC w/ C++ community edition.
    - Go to: https://visualstudio.microsoft.com/vs/features/cplusplus/
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

## To Package the app with pyinstaller
Note: you may need to turn off Windows Defender real-time protection if you get virus warning messages
during the build.

from the inno-pyinstaller directory run:
```commandline
pyinstaller -y .\w11-app.spec
```

To do a release build with the python option -OO specified, disabling asserts
and removing docstrings run the following from the inno-pyinstaller directory:
```commandline
python -OO  -m PyInstaller --clean -y .\w11-app.spec
```
Warning: If the module cffi is used, this solution will not work.  
See: https://github.com/pyinstaller/pyinstaller/issues/8252


It is very likely you will need to edit the specfile. The pyinstaller spec file is python code.
The data files for the application are put in a list of tuples. As you develop the program,
you may need to edit this list. This is a list of tuples listing the _source **file**_ and the
_destination **directory**_ in the bundle.  You can use glob syntax to specify the source files.
This is documented here: https://pyinstaller.org/en/stable/spec-files.html?highlight=datas#adding-data-files

The initial setting of datas list is:
```python
data_files = [('../myapplication/asset/*.*', './asset'),
              ('../myapplication/*.kv', '.')]
```
Successfully running Pyinstaller will create 2 directories named build and dist. The dist directory contains the exe
and the files that will be bundled with the exe.

## To package the service with pyinstaller
from the pyinstaller-service directory run:
```commandline
pyinstaller -y .\w11-svc.spec
```

To do a release build with the python option -OO specified, disabling asserts
and removing docstrings run the following from the pyinstaller-service directory:
```commandline
python -OO  -m PyInstaller --clean -y .\w11-svc.spec
```

## Create the Windows Installer
After the Cython code is built, and the App and Service have each been bundled with pyinstaller, the app and service can
be packaged into a Windows installer using innosetup.
Inno setup can be run from the GUI, open Inno Setup and select the inno-pyinstaller/full-installer.iss, the press the
"play" button to build and run the installer. The output, a Windows Installer program, will be written to
inno-pyinstaller/my-installer.exe

optionally inno setup can be run from the commandline as:
```commandline
iscc "full-installer.iss"
```
To run from the command line the path to the iscc executable must be added to the path.
"C:\Program Files (x86)\Inno Setup 6\"

The name of the output file is specified in the full-installer.iss script in the [Setup] section.

```
OutputBaseFilename=my-installer
```

this creates the output file: my-installer.exe in the inno-pyinstaller directory.
