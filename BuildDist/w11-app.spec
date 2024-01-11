# -*- mode: python ; coding: utf-8 -*-

from kivy_deps import sdl2, glew
# from myapplication.metadata import app_name_version, app_icon
from pathlib import Path

name = 'My App Name' #app_name_version
win_icon = 'C:\\Users\\ellio\\PycharmProjects\\KivyCythonWinSample\\myapplication\\asset\\cropped-cactus-512x512.ico' #Path('../myapplication') / app_icon

a = Analysis(
    ['../myapplication/trypi.py'],
    pathex=[],
    binaries=[],
    datas=[('../myapplication/asset/*.*', './myapplication/asset'),
           ('../myapplication/*.kv', './myapplication')],
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
    icon=win_icon,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    *[Tree(p) for p in (sdl2.dep_bins + glew.dep_bins)],
    strip=False,
    upx=False,
    upx_exclude=[],
    name=name,
)
