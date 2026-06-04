import csv

from db.structure.StrUser import StrUser, GeneralErrorException
import pandas as pd

from db.table.TableOperation import TableOperation


class User(TableOperation):

    def __init__(self):
        self.__users: list = []
        try:
            users = pd.read_csv("Users.csv")
            self.__users = users.values.tolist()
        except FileNotFoundError:
            self.__users = []

    def add_user(self, user: StrUser):
        if len(self.__users) <= 0:
            user.userId = '1'
            self.__users.append(user)
            to_save: list = []
            to_save.append(["UserId",
                            "Username",
                            "Password",
                            "Reminder Access"])
            for item in self.__users:
                to_save.append([item.userId,
                                item.username,
                                item.password,
                                item.get_reminder_password()])
            self.save_table("Users.csv", to_save)
        else:
            if any(user_db.username == user.username for user_db in self.__users):
                raise GeneralErrorException(f"L'utente è già presente a sistema")
            user.userId = self.__find_new_primary_key()
            self.__users.append(user)
            to_save: list = []
            for item in self.__users:
                to_save.append([item.userId,
                                item.username,
                                item.password,
                                item.get_reminder_password()])
            self.save_table("Users.csv", to_save)

    def get_user(self, index):
        return self.__users[index]

    def __find_new_primary_key(self):
        max_user_id: str = self.__users[0].userId
        for i in range(len(self.__users)):
            if max_user_id < self.__users[i].userId:
                max_user_id = self.__users[i].userId
        return (int(max_user_id) + 1).__str__()

    def print_user(self):
        for item in self.__users:
            print(item.userId + " " + item.username)

    def size(self) -> int:
        return len(self.__users)