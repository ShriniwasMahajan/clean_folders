from pathlib import Path
import os


def get_desktop_path():
    try:
        import winreg

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
        )
        desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
        return Path(desktop_path)
    except:
        return Path.home() / "Desktop"
