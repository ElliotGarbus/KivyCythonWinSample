# -*- mode: python ; coding: utf-8 -*-

import sys
sys.path.append('..')

from kivy_deps import sdl2, glew, gstreamer
from myapplication.metadata import app_name_version, app_icon
from pathlib import Path

name = app_name_version
win_icon = Path('../myapplication') / app_icon


a = Analysis(
    ['../myapplication/main.py'],
    pathex=[],
    binaries=[],
    datas=[('../myapplication/asset/*.*', './asset'),
           ('../myapplication/*.kv', '.')],
    hiddenimports=[],
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
    contents_directory='.',
    icon=[win_icon],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins + gstreamer.dep_bins)],
    strip=False,
    upx=False,
    upx_exclude=[],
    name=name,
)
