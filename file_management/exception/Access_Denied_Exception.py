class Access_Denied_Exception(Exception):
    def __init__(self, msg:str = None):
        if msg is None:
            super().__init__()
        else:
            super().__init__(msg)