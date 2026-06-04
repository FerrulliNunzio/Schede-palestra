from db.exception.GeneralErrorException import GeneralErrorException


class StrUser:

    def __init__(self, username: str = '', password: str = ''):
        self.__user_id: str = ''
        self.__username: str = username
        self.__password: str = password
        self.__reminder_pass: bool = False

    @property
    def userId(self) -> str:
        return self.__user_id

    @userId.setter
    def userId(self, user_id: str):
        if len(user_id) <= 0:
            raise GeneralErrorException()
        if len(user_id) > 8:
            raise GeneralErrorException()
        self.__user_id = user_id

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        if self.__username != '':
            raise GeneralErrorException()
        self.__username = username

    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        if self.__password != '':
            raise GeneralErrorException()
        self.__password = password

    def get_reminder_password(self) -> bool:
        return self.__reminder_pass

    def reminder_password(self):
        if self.__password is not '':
            self.__reminder_pass = True

    def clear(self):
        self.__user_id = ''
        self.__password = ''
        self.__username = ''
        self.__reminder_pass = False
