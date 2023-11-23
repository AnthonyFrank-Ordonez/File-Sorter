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


def get_file_location(path: str, file: str) -> str:
    """get the file path of the given file name"""

    # iterate the directory from its child folders or folders to get the file location it located return the absolute
    # path or full path of the file
    for root, dirs, files in os.walk(path):
        if file in files:
            return os.path.abspath(f'{root}/{file}')

    return 'The file is not in the Directory!'


def get_all_files(path: str) -> list[str]:
    """get all the files in the directory"""
    file_list: list[str] = []

    # iterate the directories to get all the files it contains and append it to list
    for root, dirs, files in os.walk(path):
        for file_names in files:
            file_list.append(file_names)

    return file_list


def set_folder_location(file: str, path: str) -> str:
    """Create and set folder based on the given file extension"""

    file_extensions: list[str] = ['png', 'webp', 'jpeg', 'jpg', 'xml', 'pdf', 'exe', 'psd', 'apk', 'mp4', 'm4a',
                                  'mp3', 'fsthumb', 'wfp', 'pptx', 'xlsx', 'lnk', 'txt', 'doc', 'docx', 'pka', 'drawio',
                                  'csv', 'rar', 'zip', 'html', 'pptm', 'css', 'eddx'
                                  ]
    new_folder: str = ''

    for extension in file_extensions:
        # if file extension endswith any extension in the file extension list then create the folder if it does not
        # exist as well as get the target location
        if file.endswith(extension) or file.endswith(extension.upper()):
            # reset and create new path
            new_folder = ''
            new_folder += os.path.join(path, extension.upper())

            # create new folder if not exists
            if not os.path.exists(new_folder):
                os.mkdir(new_folder)

    return new_folder


def sort_all_files(path: str):
    """Do the sorting and moving the files to their respective folders"""

    if file_list := get_all_files(path):

        for file in file_list:

            # find the file's present position and its target location to properly relocate it.
            current_location: str = get_file_location(path, file)
            destination_location: str = os.path.join(set_folder_location(file, path), file)

            # check if file already in the folder if not then move the file
            if not os.path.isfile(destination_location):
                shutil.move(current_location, destination_location)

        # remove any empty folder and its child folders
        remove_empty_folder(path)

    else:
        print("Your specify directory is empty... Please Input a valid path")


def main():
    """main function"""
    path: str = input("Enter the path you want to sort >> ")

    if os.path.exists(path):
        sort_all_files(path)

    else:
        print("Invalid Path...Please try again")


if __name__ == '__main__':
    main()