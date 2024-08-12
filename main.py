import sys
from PySide6.QtWidgets import QApplication
from clean_folders_app import CleanFoldersApp
from PySide6.QtGui import QIcon
import os

if __name__ == "__main__":
    app = QApplication(sys.argv)

    if getattr(sys, "frozen", False):
        application_path = sys._MEIPASS
    else:
        application_path = os.path.dirname(os.path.abspath(__file__))

    icon_path = os.path.join(application_path, "Resources", "icon.ico")
    app.setWindowIcon(QIcon(icon_path))

    window = CleanFoldersApp()
    window.show()
    sys.exit(app.exec())
