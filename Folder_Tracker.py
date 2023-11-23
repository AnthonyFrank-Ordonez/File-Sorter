import os


class FolderTracker:
    @staticmethod
    def get_file_abspath(source_path: str):
        """get all the absolute path location of each and every file"""

        file_locations: list[str] = []

        for root, dirs, files in os.walk(source_path):
            for file_names in files:
                file_locations.append(os.path.abspath(f'{root}/{file_names}'))

        return file_locations

    @staticmethod
    def newfolder_location(file: str, path: str):
        """Create and set folder based on the given file extension"""

        # split the file into two value tuple the name and the extension
        extension: str = os.path.splitext(file)[1]
        new_folder: str = ''
        new_folder += os.path.join(path, extension[1:].upper())

        if not os.path.exists(new_folder):
            os.mkdir(new_folder)

        return new_folder

    @staticmethod
    def remove_empty_folder(path: str):
        """remove any empty folder in the path"""

        for root_path, _, _ in os.walk(path, topdown=False):
            if not len(os.listdir(root_path)):
                os.rmdir(root_path)


def main():
    SetUp = FolderTracker()


if __name__ == '__main__':
    main()
