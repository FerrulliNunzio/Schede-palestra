from pathlib import Path
import pandas as pd
import tkinter as tk
from tkinter import filedialog, messagebox
import os

from file_management.exception.Access_Denied_Exception import Access_Denied_Exception
from file_management.exception.File_open_error import File_open_error
from file_management.exception.Invalid_type_exception import Invalid_type_exception
from file_management.exception.Not_supported_by_gui_exception import Not_supported_by_gui_exception
from file_management.exception.Separator_not_allowed_exception import Separator_not_allowed_exception
from file_management.exception.Wrong_parameter_Exception import Wrong_parameter_Exception


class FileManager:
    __ERROR_CODE: int = 0
    __ERROR_NOT_SUPPORTED_BY_GUI: int = -1
    __ERROR_NO_GUI: int = -2

    @staticmethod
    def open_file_dialog(windows_name: str):
        root = tk.Tk()
        root.withdraw()  # Nasconde la finestra principale di tkinter
        file_path = filedialog.askopenfilename(
            title=windows_name
        )
        root.destroy()
        return file_path

    @staticmethod
    def get_desktop_directory() -> str:
        return os.path.join(os.path.expanduser('~'), 'Desktop')

    @staticmethod
    def file_exist(file: str) -> bool:
        if FileManager.is_valid_handle() != 0:
            raise Not_supported_by_gui_exception("GUI does not support this")

        if FileManager.__contains_any(file, '*<>|"'):
            raise Wrong_parameter_Exception(f'WRONG PARAMETER Incorrect parameter: {file}')

        file = Path(file)
        if file.is_file():
            return True
        return False

    @staticmethod
    def directory_list_files(directory: str, filter: str = '.', files_only: bool = False, directory_only: bool = False,
                             count: int = 0) -> list:
        wa_file_table: str = ''
        tab: list = []
        # len: int = len(directory)
        separator_symbol: str = ''

        if FileManager.is_valid_handle() != 0:
            raise Not_supported_by_gui_exception("GUI does not support this")

        if (directory == '') or (files_only != '' and directory_only != ''):
            raise Wrong_parameter_Exception("Incorrect parameter combination")

        length: int = len(directory)
        length -= 1

        if files_only != '':
            files_only = True
        elif directory_only != '':
            directory_only = True

        file_table: list = []

        if files_only != '':
            file_table = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        elif directory_only != '':
            file_table = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
        else:
            file_table = os.listdir(directory)

        count = len(file_table)
        return file_table

    @staticmethod
    def directory_create(directory: str):
        if not os.path.exists(directory):
            os.makedirs(directory)

    @staticmethod
    def download_file(filename: str, data_tab: list, filetype: str = "ASC", append: str = "",
                      write_field_separator: str = "", confirm_overwrite: bool = False):

        append_mode: str = append

        if filetype == "BIN" or filetype == "ASC" or filetype == "DAT":
            pass
        else:
            raise Invalid_type_exception("Valore non valido per il parametro FILETYPE")

        if filetype == "BIN" and write_field_separator != '':
            raise Separator_not_allowed_exception("Il separatore non è consentito.")

        if not confirm_overwrite or append != '':
            if FileManager.file_exist(filename):
                result = messagebox.askyesno(title="Conferma", message="Il file deve essere sovrascritto?")
                if not result:
                    raise Access_Denied_Exception("Accesso al file negato.")
            else:
                if append != '':
                    append_mode = ""

        export = pd.DataFrame(data_tab)
        template_path = filename

        if filetype == "BIN":
            if append_mode == 'X':
                writer = pd.ExcelWriter('test.xlsx', engine='openpyxl', mode='a')
                export.to_excel(writer, sheet_name='Sheet1')
                writer.save()
            else:
                export.to_excel(template_path, sheet_name='Sheet1', index=False, )
        else:
            if append_mode == 'X':
                export.to_csv(template_path, index=False, mode='a')
            else:
                export.to_csv(template_path, index=False)

    @staticmethod
    def upload_file(filename: str, filetype: str = 'ASC', has_field_separator: str = "") -> pd.DataFrame:

        # if filetype == 'BIN' and has_field_separator != "":
        if filetype == 'BIN' and has_field_separator != '':
            raise Separator_not_allowed_exception("Il separatore non è consentito.")

        if not FileManager.file_exist(filename):
            raise File_open_error("File non trovato, impossibile aprirlo.")

        if filetype == "BIN":
            return pd.read_excel(filename)
        elif filetype == 'ASC':
            return pd.read_csv(filename)
        elif filetype == 'DAT':
            return pd.read_csv(filename)
        else:
            raise Invalid_type_exception("Valore non valido per il parametro FILETYPE.")

    @staticmethod
    def is_valid_handle():
        rcode: int = FileManager.__ERROR_CODE
        if rcode == FileManager.__ERROR_NOT_SUPPORTED_BY_GUI:
            rcode = FileManager.__ERROR_NOT_SUPPORTED_BY_GUI
        elif rcode == FileManager.__ERROR_NO_GUI:
            rcode = FileManager.__ERROR_NO_GUI
        return rcode

    @staticmethod
    def __contains_any(str1: str, str2: str) -> bool:
        contain: bool = False
        for i in range(len(str2)):
            if str2[i] in str1:
                contain = True
        return contain