import os
import shutil
import time
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox
from Folder_Tracker import FolderTracker as Ft


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

        # Set Up the grid and position of all the elements 
        self.select_folder_textbox.grid(rowspan=5, column=1, pady=20)
        self.select_folderBtn.grid(row=1, column=0, padx=20, pady=15)
        self.sort_folderBtn.grid(row=2, column=0)
        self.status_label.grid(row=5, columnspan=2)
        self.statusMsg_label.grid(row=6, columnspan=2)

    def select_folder(self):
        """Select the Folder Path the user wants to sort"""

        # Unlocked the textbox and prompt the user to select a folder
        self.select_folder_textbox.configure(state=ctk.NORMAL)
        selected_folder_path = ctk.filedialog.askdirectory()

        if selected_folder_path:
            # delete the all text from the textbox and insert new value
            self.select_folder_textbox.delete(1.0, ctk.END)
            self.select_folder_textbox.insert(1.0, selected_folder_path)
            
            # Locked the Textbox and update the status message label
            self.select_folder_textbox.configure(state=ctk.DISABLED)
            self.statusMsg_label.configure(text="Sort the selected folder by clicking the Sort Button",
                                           text_color='Grey')

    def sort_files(self):
        """Do the sorting and moving the files to their respective folders"""
        # get the value or text from the textbox before the newline and update the label
        source_path: str = self.select_folder_textbox.get('1.0', 'end-1c')
        self.statusMsg_label.configure(text="Sorting your Files, Please Wait...", text_color='White')

        if file_location := Ft.get_file_abspath(source_path):
            # iterate each of the absolute path of all the file then process all the required values
            for absFile_location in file_location:
                file_name: str = absFile_location.split("\\")[-1]
                
                # desstination location
                destination: str = os.path.join(Ft.newfolder_location(file_name, source_path), file_name)

                # if file is still not in folder move the file else pass
                if not os.path.isfile(destination):
                    shutil.move(absFile_location, destination)

            # remove the empty folders after moving all the files and update again the label
            Ft.remove_empty_folder(source_path)
            CTkMessagebox(message='File Sorted Successfully!', option_1='OK', icon='check')
            time.sleep(2)
            self.statusMsg_label.configure(text='Waiting to Start, PLease Select a Folder', text_color="Red")

    def run_app(self):
        """run the app"""
        self.window.mainloop()


def main():
    """main method"""
    # Create the object of the FileSorter
    FS = FileSorter()
    FS.run_app()


if __name__ == '__main__':
    """Initializer"""
    main()
