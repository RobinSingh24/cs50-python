# Downloads Cleaner
#### Video Demo:  https://youtu.be/sGBl2PkaTbA
## Description
Hi all! This is my final project for the CS50 Python course. This project makes maintaining your downloads folder much easier. The 'Download Cleaner' scans through your downloads folder and organizes your files into respective sub-folder categories. This project aims to reduce clutter and improve readability without going through the files manually.

Beyond the initial convenience, this project addresses a common digital hygiene problem that plagues almost every computer user. Over time, the "Downloads" folder often becomes a repository for miscellaneous files—PDFs from work, images from the web, installers, and compressed archives. Manually sorting these is a tedious, low-priority task that many users neglect for months, leading to a "digital junk drawer" effect. My script automates this process entirely by acting as a background digital organizer, transforming a chaotic list of files into a structured system of folders.

### Technical Implementation and Design
The core logic of the Download Cleaner is built on a modular architecture to ensure the code is both readable and maintainable. It utilizes the `pathlib` library to handle file paths in a modern, cross-platform manner. By using `Path.home()`, the script can dynamically locate the user's home directory regardless of whether they are on Windows, macOS, or Linux. This was a critical design choice; I wanted to ensure that the tool was accessible to a wide audience without requiring the user to manually type in their folder paths.



To perform the physical organization, the script relies on a dictionary-driven mapping system. This design choice was made to ensure scalability and clean code. Instead of using complex, nested conditional trees or dozens of `if-elif` statements, the program loops through a clean dictionary where keys represent folder names (like "Images" or "Documents") and values are lists of associated extensions (like ".jpg", ".png", or ".pdf"). This makes the code much easier to update in the future—if I want to add a new category for "Video Files," I simply add a single line to the dictionary rather than rewriting the movement logic. Once a file is identified, the `shutil` library is used to physically relocate the file.

### Reliability and Safety
Safety was a primary concern during the development phase because a script with the power to move files must be "fail-safe" to prevent data loss. I implemented robust exception handling using `try-except` blocks to manage common system hurdles. For example, if a file is currently open in another application, the script will catch a `PermissionError`, notify the user through the terminal, and move on to the next file rather than crashing the entire process. Similarly, it handles `FileNotFoundError` gracefully if a file is deleted or moved by another process during the scan.



### Testing and UX
To enhance the User Experience (UX), the script features an integrated ASCII art banner generated via the `pyfiglet` library. This provides a professional "software" feel to the command-line interface immediately upon launch. For quality assurance, I utilized `pytest` combined with a sophisticated mocking strategy. By using `unittest.mock.patch`, I was able to verify that the file-moving logic works perfectly without needing to actually manipulate my own hard drive during every test run. This ensures that the code is "bulletproof" before it ever touches a user's real data.



Ultimately, this project represents a practical application of the core skills learned in CS50P—string manipulation, dictionary mapping, file I/O, error handling, and unit testing—all coming together to create a tool that saves time and makes digital life just a little bit more organized.
