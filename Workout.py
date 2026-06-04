import pandas as pd
import pickle

from db.table.Exercise import Exercise


class Workout:

    def __init__(self, workout_name: str):
        self.__workout_name: str = workout_name
        self.__exercises: list = []

    def add_exercise(self, exercise: Exercise):
        self.__exercises.append(exercise)

    def __str__(self):
        out: str = ''

        out += self.__workout_name + '\n\n\n'

        for item in self.__exercises:
            out += item.__str__() + '\n\n'
        return out
