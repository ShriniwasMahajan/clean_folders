# Clean Folders

Clean Fodlers is a cross-platform desktop application that helps you organize files in specified folders automatically.

## Features

- Automatically sorts files based on their extensions
- Monitors specified folders for changes
- User-friendly graphical interface

## Installation

1. Go to the [Releases](https://github.com/yourusername/clean_folders/releases) page.
2. Download the latest version for your operating system.
3. Extract the downloaded file.
4. Run the executable file named `Clean Folders`.

## Usage

1. Launch the app.
2. Enter the folder paths you want to monitor, separated by semicolons.
3. Click the "Start" button to begin monitoring and sorting.
4. Click the "Stop" button when you want to stop the process.

## Building from Source

If you want to build the app from source:

1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install the requirements: `pip install -r requirements.txt`
4. Install PyInstaller: `pip install pyinstaller`
5. Run: `pyinstaller clean_folders_app.spec`

## Requirements

- Python 3.6 or higher
