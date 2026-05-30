import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename="operations.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Audio": [".mp3", ".wav"],
    "Videos": [".mp4", ".avi", ".mkv"],
    "Archives": [".zip", ".rar"]
}


def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return "Others"


def organize_files(folder_path):
    try:
        files = os.listdir(folder_path)

        for file in files:

            file_path = os.path.join(folder_path, file)

            if os.path.isfile(file_path):

                _, extension = os.path.splitext(file)

                category = get_category(extension)

                category_folder = os.path.join(folder_path, category)

                if not os.path.exists(category_folder):
                    os.makedirs(category_folder)

                destination = os.path.join(category_folder, file)

                shutil.move(file_path, destination)

                print(f"Moved: {file} → {category}")

                logging.info(
                    f"{file} moved to {category}"
                )

        print("\nFile Organization Completed Successfully!")

    except FileNotFoundError:
        print("Folder not found!")

    except PermissionError:
        print("Permission denied!")

    except Exception as e:
        print("Unexpected Error:", e)


if __name__ == "__main__":

    folder = input("Enter folder path: ")

    organize_files(folder)