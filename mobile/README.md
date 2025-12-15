# Mobile app (Kivy + KivyMD) for ML PROJECT

Quick start (desktop/emulator)

1. Create and activate a virtual environment (Windows example):

```bash
python -m venv .venv_mobile
.venv_mobile\Scripts\activate
pip install -r mobile/requirements.txt
```

2. Run the app on desktop (for development):

```bash
python mobile/main.py
```

Android build notes

- Building an APK requires Buildozer / python-for-android which runs on Linux.
- On Windows, install WSL (Ubuntu) or use a Linux VM. Then run Buildozer from the repo root.

Example (WSL) commands:

```bash
# from Windows PowerShell: open WSL in repo folder
wsl
cd "/mnt/c/Users/Admin/Documents/ml project folder/ML PROJECT ALMOST"
python3 -m pip install --user --upgrade buildozer
sudo apt update && sudo apt install -y build-essential git python3-pip openjdk-11-jdk
buildozer android debug deploy run
```

Notes

- The mobile app reuses existing project modules when available (it imports from the parent project root).
- For charts we use `kivy_garden.graph`. If you need richer charts consider `matplotlib` or external webview charts.
- The `buildozer.spec` provided is a minimal template — customize permissions, icons, and requirements as needed before packaging.
