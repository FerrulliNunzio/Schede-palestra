from pathlib import Path

class Setting:
    screen_size: str = ''

    def __init__(self):
        file = Path(r"C:\SchedePalestra\Settings.csv")

        if not file.is_file():
            print("crea file")