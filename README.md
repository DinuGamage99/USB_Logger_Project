# 🔐 USB Logger and Unauthorized Device Detector

This is a Python-based security tool that continuously monitors USB device connections. It alerts you with a beep sound and popup if an unauthorized USB device is connected.

## 🚀 Features

- Detects all USB device insertions and removals
- Compares connected USBs with an authorized list
- Alerts user with sound and popup if unauthorized USB is detected
- Logs events with timestamps in logs.txt

## ✅ Requirements

- Windows OS
- Python 3.10+
- Python Packages:
  - wmi
  - pywin32
  - pymsgbox

Install them via:
```bash
pip install pywin32 wmi pymsgbox
