class Not_supported_by_gui_exception(Exception):

    def __init__(self, msg: str = ''):
        super().__init__(msg)