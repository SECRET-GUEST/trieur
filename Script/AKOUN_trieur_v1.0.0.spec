# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['YOUR PATH \\html\\AKOUN_trieur_v1.0.0.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('YOUR PATH \\html\\tuto.html', 'html'),
        ('YOUR PATH \\ico\\trieur.png', 'ico'),
        ('YOUR PATH \\lib\\common.py', 'lib'),
        ('YOUR PATH \\css\\dark.css', 'css'),
        ('YOUR PATH \\light.css', 'css')
    ],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='AKOUN_trieur_v1.0.0',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='YOUR PATH \\ico\\trieur.ico',
)

# Optional: use UPX to compress the executable
# You need to have UPX installed and added to the system PATH for this to work
# See https://upx.github.io/ for more information
import os
upx_path = 'upx'  # Change to the path of UPX if it's not in the system PATH
if os.path.exists(upx_path):
    exe.upx = True
    exe.upx_args.append('--lzma')
else:
    print('WARNING: UPX not found in system PATH, executable will not be compressed')
