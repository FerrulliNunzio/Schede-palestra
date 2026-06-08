class File_open_error(Exception):
    def __init__(self, msg: str = ""):
        super().__init__(msg)