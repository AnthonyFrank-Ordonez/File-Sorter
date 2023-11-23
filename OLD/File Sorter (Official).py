import os
import shutil
import time

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class FileSorter:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title('FILE SORTER')
        self.window.geometry('390x270')
        self.window.resizable(False, False)

        # Buttons, Labels, Textbox, etc.:
        self.select_folderBtn = ctk.CTkButton(self.window,
                                              text="Select Folder",
                                              height=55,
                                              font=('Calibri Bold', 15),
                                              command=self.select_folder
                                              )

        self.sort_folderBtn = ctk.CTkButton(self.window,
                                            text='Sort Files',
                                            height=55,
                                            font=('Calibri Bold', 15),
                                            command=self.sort_files
                                            )

        self.status_label = ctk.CTkLabel(self.window,
                                         text='Status: ',
                                         text_color='White',
                                         font=('Calibri Bold', 15)
                                         )

        self.statusMsg_label = ctk.CTkLabel(self.window,
                                            text='Waiting to Start, PLease Select a Folder',
                                            text_color="Red",
                                            font=('Calibri Bold', 15)
                                            )

        self.select_folder_textbox = ctk.CTkTextbox(self.window, height=150)

        # Insert placeholder text in textbox
        self.select_folder_textbox.insert(1.0, text='Folder Path')

        # Set Up Grid
        self.select_folder_textbox.grid(rowspan=5, column=1, pady=20)
        self.select_folderBtn.grid(row=1, column=0, padx=20, pady=15)
        self.sort_folderBtn.grid(row=2, column=0)
        self.status_label.grid(row=5, columnspan=2)
        self.statusMsg_label.grid(row=6, columnspan=2)

    def select_folder(self):
        """Select the Folder Path the user wants to sort"""

        self.select_folder_textbox.configure(state=ctk.NORMAL)
        selected_folder_path = ctk.filedialog.askdirectory()

        if selected_folder_path:
            self.select_folder_textbox.delete(1.0, ctk.END)
            self.select_folder_textbox.insert(1.0, selected_folder_path)
            self.select_folder_textbox.configure(state=ctk.DISABLED)
            self.statusMsg_label.configure(text="Sort the selected folder by clicking the Sort Button",
                                           text_color='Grey')

    def sort_files(self):
        """Do the sorting and moving the files to their respective folders"""
        source_path: str = self.select_folder_textbox.get('1.0', 'end-1c')

        self.statusMsg_label.configure(text="Sorting your Files, Please Wait...", text_color='White')

        if file_location := self.get_file_abspath(source_path):
            for absFile_location in file_location:
                file_name: str = absFile_location.split("\\")[-1]
                destination: str = os.path.join(self.newfolder_location(file_name, source_path), file_name)

                # if file is still not in folder move the file else pass
                if not os.path.isfile(destination):
                    shutil.move(absFile_location, destination)

            # remove the empty folders after moving all the files
            self.remove_empty_folder(source_path)
            CTkMessagebox(message='File Sorted Successfully!', option_1='OK', icon='check')
            time.sleep(2)
            self.statusMsg_label.configure(text='Waiting to Start, PLease Select a Folder', text_color="Red")

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
                print(f"Path: {root_path} have been removed successfully!")

    def run_app(self):
        self.window.mainloop()


def main():
    FS = FileSorter()
    FS.run_app()


if __name__ == '__main__':
    main()
