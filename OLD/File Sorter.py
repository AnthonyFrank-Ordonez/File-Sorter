import os
import shutil


def remove_empty_folder(path: str):
    """remove any empty folder in the path"""

    for root_path, _, _ in os.walk(path, topdown=False):

        if not len(os.listdir(root_path)):
            os.rmdir(root_path)
            print(f"Path: {root_path} have been removed successfully!")

    print("Sorting Complete!")


def get_file_location(path: str, file: str) -> str:
    """get the file path of the given file name"""

    for root, dirs, files in os.walk(path):
        if file in files:
            return os.path.abspath(f'{root}/{file}')

    return 'The file is not in the Directory!'


def get_all_files(path: str) -> list[str]:
    """get all the files in the directory"""
    file_list: list[str] = []

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
        if file.endswith(extension) or file.endswith(extension.upper()):
            new_folder = ''
            new_folder += os.path.join(path, extension.upper())

            if not os.path.exists(new_folder):
                os.mkdir(new_folder)

    return new_folder


def sort_all_files(path: str):
    """Do the sorting and moving the files to their respective folders"""

    if file_list := get_all_files(path):

        for file in file_list:
            current_location: str = get_file_location(path, file)
            destination_location: str = os.path.join(set_folder_location(file, path), file)

            if not os.path.isfile(destination_location):
                shutil.move(current_location, destination_location)

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