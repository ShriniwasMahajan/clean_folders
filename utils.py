from pathlib import Path
import os


def get_desktop_path():
    try:
        # Try to get the desktop path using the Windows API
        import winreg

        key = winreg.OpenKey(
            winreg.HKEY_CURRENT_USER,
            r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders",
        )
        desktop_path = winreg.QueryValueEx(key, "Desktop")[0]
        return Path(desktop_path)
    except:
        # Fallback to the standard desktop location
        return Path.home() / "Desktop"
