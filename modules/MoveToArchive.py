import os
import shutil


def move_file_to_archive(file_path, archive_folder):
    if not file_path:
        return None

    if not os.path.exists(file_path):
        print(f"Archive skipped, file not found: {file_path}")
        return None

    os.makedirs(archive_folder, exist_ok=True)

    file_name = os.path.basename(file_path)
    destination = os.path.join(archive_folder, file_name)

    name, extension = os.path.splitext(file_name)
    counter = 1
    while os.path.exists(destination):
        destination = os.path.join(archive_folder, f"{name}_{counter}{extension}")
        counter += 1

    shutil.move(file_path, destination)
    print(f"Moved file to archive: {destination}")
    return destination