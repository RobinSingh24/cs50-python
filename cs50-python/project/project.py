import os
import shutil
import pyfiglet
from sys import exit


def main():

    print(welcome())

    # For the sake of codespaces using below approach
    # Replace the below path with Path.home()/Downloads if running in your local system
    downloads_dir = "./downloads"
    if not os.path.exists(downloads_dir):
        os.makedirs(downloads_dir)
        exit(f"Created {downloads_dir}. Put some files in downloads and run again!")

    files = [
        file
        for file in os.listdir(downloads_dir)
        if os.path.isfile(os.path.join(downloads_dir, file))
    ]

    #  move files to their respective category folders
    moved_count = 0
    for file in files:
        category = get_category(file)
        if category != "Others":
            move_file(downloads_dir, file, category)
            moved_count += 1

    if moved_count > 0:
        print(f"Cleaned up {moved_count} files")
    else:
        print("No files to clean")


def get_category(filename):
    """Returns file category based on the filename"""
    file_ext = os.path.splitext(filename)[1].lower()
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".txt", ".docx", ".xlsx", ".pptx"],
        "Music": [".mp3", ".aac", ".wav"],
        "Videos": [".mp4", ".mov", ".avi"],
        "Compressed": [".rar", ".zip", ".tar"],
    }

    for category, extensions in categories.items():
        if file_ext in extensions:
            return category

    return "Others"


def move_file(root, file, category):
    """Moves file into the category subfolder"""
    target_dir = os.path.join(root, category)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    source = os.path.join(root, file)
    destination = os.path.join(target_dir, file)

    try:
        shutil.move(source, destination)
    except:
        print("Exception occured")

    return True


def welcome():
    return pyfiglet.figlet_format("Downloads cleaner", font="small")


if __name__ == "__main__":
    main()
