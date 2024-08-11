import sys
from PySide6.QtWidgets import QApplication
from clean_desktop_app import CleanDesktopApp
from PySide6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("Resources\icon.ico"))
    window = CleanDesktopApp()
    window.show()
    sys.exit(app.exec())
