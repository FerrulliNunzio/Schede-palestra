class Wrong_parameter_Exception(Exception):
    def __init__(self, msg: str = ''):
        super().__init__(msg)