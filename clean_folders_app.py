from PySide6.QtWidgets import (
    QMainWindow,
    QVBoxLayout,
    QWidget,
    QPushButton,
    QLabel,
    QTextEdit,
    QHBoxLayout,
    QMessageBox,
    QLineEdit,
    QApplication,
)
from PySide6.QtCore import QTimer
from pathlib import Path
from event_handler import EventHandler
from utils import get_desktop_path


class CleanFoldersApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clean Folders")
        self.setWindowIcon(QApplication.windowIcon())
        self.setGeometry(100, 100, 500, 400)

        self.init_ui()
        self.event_handlers = []
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.sort_files)

    def init_ui(self):
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        self.folder_input = QLineEdit(str(get_desktop_path()))
        self.folder_input.setPlaceholderText(
            "Enter folder paths separated by semicolons (;)"
        )
        layout.addWidget(QLabel("Folders to organize:"))
        layout.addWidget(self.folder_input)

        self.status_label = QLabel("Status: Not running")
        layout.addWidget(self.status_label)

        button_layout = QHBoxLayout()
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_cleaning)
        button_layout.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop_cleaning)
        self.stop_button.setEnabled(False)
        button_layout.addWidget(self.stop_button)

        layout.addLayout(button_layout)

        self.log_text = QTextEdit()
        self.log_text.setReadOnly(True)
        layout.addWidget(self.log_text)

    def start_cleaning(self):
        folders = [
            Path(folder.strip())
            for folder in self.folder_input.text().split(";")
            if folder.strip()
        ]

        if not folders:
            QMessageBox.warning(
                self, "Warning", "Please enter at least one folder path."
            )
            return

        try:
            for folder in folders:
                if not folder.exists():
                    raise FileNotFoundError(f"Folder not found: {folder}")

                sorted_files_path = folder / "Holder of Things"
                sorted_files_path.mkdir(exist_ok=True)

                event_handler = EventHandler(folder, sorted_files_path)
                event_handler.file_moved.connect(self.log_file_moved)
                self.event_handlers.append(event_handler)

                self.log_text.append(f"Watching: {folder}")
                self.log_text.append(f"Sorting to: {sorted_files_path}")

            self.sort_files()  # Initial sort
            self.timer.start(60000)  # Check every 60 seconds

            self.status_label.setText("Status: Running")
            self.start_button.setEnabled(False)
            self.stop_button.setEnabled(True)
            self.folder_input.setEnabled(False)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to start cleaning: {str(e)}")
            self.stop_cleaning()

    def stop_cleaning(self):
        self.timer.stop()
        self.event_handlers.clear()
        self.status_label.setText("Status: Stopped")
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)
        self.folder_input.setEnabled(True)

    def sort_files(self):
        for handler in self.event_handlers:
            try:
                handler.sort_directory()
            except Exception as e:
                self.log_text.append(f"Error during sorting: {str(e)}")

    def log_file_moved(self, source, destination):
        self.log_text.append(f"Moved: {source} -> {destination}")
