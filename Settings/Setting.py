from pathlib import Path
from file_management.FileManager import FileManager


class Setting:

    SETTING_PATH: str = r"C:\SchedePalestra\Settings.csv"

    screen_size: str = ''
    language: str = ''

    def __init__(self):
        if not FileManager.file_exist(Setting.SETTING_PATH):
            Setting.screen_size = '500x300'
            to_save: list = [Setting.screen_size]
            FileManager.download_file(filename=Setting.SETTING_PATH, data_tab=to_save)
        else:
            file = FileManager.upload_file(Setting.SETTING_PATH)
            file_list = file.values.tolist()
            Setting.screen_size = file_list[0][0]

    @staticmethod
    def change_screen_size(new_screen_size: str):
        Setting.screen_size = new_screen_size
        to_save: list = [Setting.screen_size]
        FileManager.download_file(filename=Setting.SETTING_PATH, data_tab=to_save, confirm_overwrite=True)
