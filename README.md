# Simple QR Code App

A lightweight, offline QR code generator and reader built with Python and Tkinter.  
Works on Windows, macOS, and Linux.

## Quick Start

```bash
git clone https://github.com/youruser/simple-qr-code-app.git
cd simple-qr-code-app
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
python qr-code-app.py
```

## End‑User Guide

- **Generate a QR Code** – Type text or a URL, click **Generate QR Code**.  
  The image appears below; click **Save QR Code** to export as PNG.
- **Read from Camera** – Click **Read QR Code from Camera** and point the webcam at a QR code.  
  The decoded data pops up; press **q** to stop the camera.

## Developer Guide

### Project layout

```
qr-code-app.py          # Main application
requirements.txt        # Python dependencies
```

### Dependencies

```text
opencv-python
pillow
qrcode[pil]
```

> `tkinter` is bundled with Python on Windows/macOS.  
> On Linux you may need `python3-tk`.

### Building a standalone executable

```bash
pip install pyinstaller
# On Linux/macOS
pyinstaller --onefile qr-code-app.py
# On Windows (run the command on a Windows machine)
pyinstaller --onefile qr-code-app.py
```

The executable will be located in `dist/`.

## Contributing

1. Fork the repository.  
2. Create a topic branch: `git checkout -b feat/…`.  
3. Run the app and any tests you add.  
4. Open a pull request.

## License

MIT © 2026 Simple QR Code App