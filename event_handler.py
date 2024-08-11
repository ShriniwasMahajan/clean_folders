import shutil
from pathlib import Path
from PySide6.QtCore import QObject, Signal
from extensions import extensionPaths


class EventHandler(QObject):
    file_moved = Signal(str, str)

    def __init__(self, watch_path: Path, destination_root: Path):
        super().__init__()
        self.watch_path = watch_path
        self.destination_root = destination_root

    def sort_directory(self):
        for file in self.watch_path.iterdir():
            if file.is_file() and file.suffix.lower() in extensionPaths:
                self.move_file(file)

    def move_file(self, file: Path):
        destination_folder = self.destination_root / extensionPaths[file.suffix.lower()]
        destination_folder.mkdir(parents=True, exist_ok=True)

        new_file_path = destination_folder / file.name
        if new_file_path.exists():
            new_file_path = self.rename_file(new_file_path)

        shutil.move(str(file), str(new_file_path))
        self.file_moved.emit(str(file), str(new_file_path))

    def rename_file(self, file_path: Path):
        counter = 1
        while file_path.exists():
            new_name = f"{file_path.stem}_{counter}{file_path.suffix}"
            file_path = file_path.with_name(new_name)
            counter += 1
        return file_path
