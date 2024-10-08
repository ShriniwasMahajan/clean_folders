# Clean Folders

Clean Folders is a cross-platform desktop application designed to automatically organize files in specified folders, streamlining your workflow by keeping your directories tidy.

## Features

- **Automatic Sorting**: Automatically sorts files based on their extensions and creation date.
- **Multi-Path Monitoring**: Simultaneously tracks multiple folder paths, with the default path set to the desktop location.
- **Real-Time Logs**: Provides detailed logs of file movements, so you can keep track of every action performed by the app.
- **Folder Monitoring**: Continuously monitors specified folders for changes, instantly reacting to new or modified files.
- **User-Friendly Interface**: Intuitive and accessible graphical user interface, making it easy for users of all levels to manage their files.

## Installation

### Download Setup Files

- **Windows**: [Clean.Folders.exe](https://github.com/ShriniwasMahajan/clean_folders/releases/download/v1.0.0/Clean.Folders.exe)

![Screenshot 2024-08-12 171624](https://github.com/user-attachments/assets/1fe506a1-966b-4252-80f1-2492f2b81984)

- **MacOS**: [Clean.Folders.app.zip](https://github.com/ShriniwasMahajan/clean_folders/releases/download/v1.0.0/Clean.Folders.app.zip)

![Image (1)](https://github.com/user-attachments/assets/13d9d63b-5bdb-44ba-83e2-1de47a4c5537)

## Requirements

- Python 3.6 or higher

## Usage

1. Launch the app.
2. Enter the folder paths you want to monitor, separated by semicolons.
3. Click the "Start" button to begin monitoring and sorting files within the specified directories.
4. View real-time logs of file movements in the application window to track how your files are being organized.
5. Click the "Stop" button when you want to stop the process.

## Building from Source

If you want to build the app from source:

1. Clone this repository using Git:
   ```bash
   git clone https://github.com/ShriniwasMahajan/clean_folders.git
   ```
2. Navigate to the project directory:
   ```bash
   cd clean_folders
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Install PyInstaller, which is required to create an executable:
   ```bash
   pip install pyinstaller
   ```
6. Create an approproate .spec file and then:
   ```bash
   pyinstaller clean_folders.spec
   ```
7. The built application will be located in the dist directory.
