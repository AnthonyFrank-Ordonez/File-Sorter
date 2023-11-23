import os
import shutil


def remove_empty_folder(path: str):
    """remove any empty folder in the path"""

    for root_path, _, _ in os.walk(path, topdown=False):
        # iterate all the folders and sub folders in the path to check if there are any empty folders or sub folders if
        # there are empty folder then the folder will be removed from the directory E.G:

        # disk letter:/home_folder/folder/sub folders/another sub folders
        # []

        if not len(os.listdir(root_path)):
            os.rmdir(root_path)
            print(f"Path: {root_path} have been removed successfully!")

    print("Sorting Complete!")


def get_file_abspath(path: str):
    """get all the absolute path location of each and every file"""

    file_locations: list[str] = []

    for root, dirs, files in os.walk(path):
        for file_names in files:
            file_locations.append(os.path.abspath(f'{root}/{file_names}'))

    return file_locations


def set_folder_location(file: str, path: str) -> str:
    """Create and set folder based on the given file extension"""

    # split the file name into two tuple values (file_name, extension)
    extension: str = os.path.splitext(file)[1]
    # reset the path of the new folder every call
    new_folder: str = ''
    # create the path of the extension folder
    new_folder += os.path.join(path, extension[1:].upper())

    # if the extension folder does not exist create the folder else just return the new_folder path
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)

    return new_folder


def sort_all_files(path: str):
    """Do the sorting and moving the files to their respective folders"""

    if file_location := get_file_abspath(path):
        # iterate all the abs location of all the files in the path specified
        for file_path_location in file_location:
            # get the file name using split and subscription expression
            file_name = file_path_location.split("\\")[-1]
            # get the destination location to move the file based on its extension
            destination_location: str = os.path.join(set_folder_location(file_name, path), file_name)

            # if file is still not in folder move the file else pass
            if not os.path.isfile(destination_location):
                shutil.move(file_path_location, destination_location)

        # remove the empty folders after moving all the files
        remove_empty_folder(path)


def main():
    """main function"""
    path: str = input("Enter the path you want to sort >> ")

    if os.path.exists(path):
        sort_all_files(path)

    else:
        print("Invalid Path...Please try again")


if __name__ == '__main__':
    main()