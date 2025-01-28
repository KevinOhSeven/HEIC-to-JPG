# Bulk HEIC to JPG Converter

![image](https://github.com/user-attachments/assets/c5c068a6-6c84-407e-8509-be28f53c01fe)


## Overview
The **Bulk HEIC to JPG Converter** is a simple, user-friendly desktop application for Windows that converts multiple HEIC image files to JPG format. It features a modern graphical interface for ease of use, making it suitable for photographers, content creators, and everyday users.

![image](https://github.com/user-attachments/assets/6a1bf960-d1cc-4bc9-b365-9a26b3b3a3e1)

## Features
- Bulk convert multiple HEIC files to JPG with a few clicks.
- Modern, intuitive graphical user interface (GUI).
- Select your desired output directory for converted files.
- Lightweight and portable, no installation required.

## Requirements
If using the `.exe` file:
- No additional setup required.

If running from the source code:
- Python 3.9 or later
- Required Python libraries:
  - `pillow-heif`
  - `tkinter`
  - `pyinstaller` (optional, for creating `.exe`)

Install dependencies with: pip install pillow-heif tk pyinstaller


## How to Use
1. Download the latest release from the [Releases](https://github.com/your-repo/releases) section.
2. Run the `.exe` file.
3. Use the GUI to:
   - Select HEIC files to convert.
   - Choose the output directory.
4. Click **Convert**, and your images will be saved as JPG files in the chosen folder.

## Installation (For Developers)
To run or modify the project from the source:
1. Clone the repository: git clone https://github.com/your-repo/heic-converter.git

2. Install dependencies: pip install -r requirements.txt

3. Run the script: python heic_converter.py

4. (Optional) Create an executable: pyinstaller --onefile --windowed heic_converter.py


## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your changes.
3. Submit a pull request.

## License
This project is licensed under the Apache License 2.0. See the `LICENSE` file for details.

## Support
If you encounter issues or have questions, open an issue in the [Issues](https://github.com/your-repo/issues) section.

## Acknowledgments
- Built using Python, Tkinter, and `pillow-heif`.
- Created to simplify working with modern HEIC image formats.


