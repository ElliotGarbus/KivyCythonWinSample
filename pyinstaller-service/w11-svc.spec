# -*- mode: python ; coding: utf-8 -*-
import sys
sys.path.append('..')

from myapplication.metadata import service_name, service_icon
from pathlib import Path


name = service_name
win_icon = Path('../myapplication') / service_icon

a = Analysis(
    ['..\\myservice\\main.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=['mylibrary', 'win32timezone'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=[win_icon],
    contents_directory='.',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name=name,
)
