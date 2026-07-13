# -*- mode: python ; coding: utf-8 -*-
import sys

a = Analysis(
    ['qr-code-app.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[
        'qrcode.image.pil',
        'qrcode.image.base',
        'PIL._tkinter_finder',
        'cv2',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='qr-code-app',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

# macOS: empacota num .app com permissão de câmara declarada
if sys.platform == 'darwin':
    app = BUNDLE(
        exe,
        name='QR Code App.app',
        bundle_identifier='com.qrcodeapp',
        info_plist={
            'NSCameraUsageDescription': 'Esta aplicação precisa de aceder à câmara para ler QR Codes.',
            'NSHighResolutionCapable': True,
            'CFBundleShortVersionString': '1.0.0',
            'CFBundleName': 'QR Code App',
        },
    )
