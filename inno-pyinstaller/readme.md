This directory contains pyinstaller and innosetup files and working directories.
The pyinstaller file w11-app.spec is used to build the app into an exe.
* The subdirectory "build" is pyinstaller working directory.
* The subdirectory "dist" is the pyinstaller output directory. The contents of this directory is used by inno-setup.

The inno setup file "appinstaller.iss" creates the installer "MyAppInstaller.exe".

todo: use relative paths in .iss file or set the base directory with a #define
todo: in iss file remove version from exe name

