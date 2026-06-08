class Separator_not_allowed_exception(Exception):
    def __init__(self, msg: str = ""):
        super().__init__(msg)