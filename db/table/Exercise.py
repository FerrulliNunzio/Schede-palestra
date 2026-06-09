import pandas as pd

from db.structure.StrExercise import StrExercise
from db.table.TableOperation import TableOperation


class Exercise(TableOperation):

    def __init__(self):
        self.__exercise: list = []
        try:
            workout = pd.read_csv(r"C:\SchedePalestra\Exercises.csv")
            lst = workout.values.tolist()
            for item in lst:
                self.__exercise.append(StrExercise(item[0], item[1]))
        except FileNotFoundError:
            self.__exercise = []

    def get(self):
        return self.__exercise

    def add_exercise(self, exercise: StrExercise):
        if len(self.__exercise) <= 0:
            exercise.id_exercise = 1
            self.__exercise.append(exercise)
            to_save: list = []
            to_save.append([
                'exercise_id',
                'name',
            ])
            for item in self.__exercise:
                to_save.append([item.id_exercise,
                                item.name,
                                ])
            self.save_table(r"C:\SchedePalestra\Exercises.csv", to_save)
        else:
            exercise.workout_exercise_id = self.find_new_primary_key()
            self.__exercise.append(exercise)
            to_save: list = []
            to_save.append([
                'exercise_id',
                'name',
            ])
            for item in self.__exercise:
                to_save.append([item.id_exercise,
                                item.name,
                                ])
            self.save_table(r"C:\SchedePalestra\Exercises.csv", to_save)

    def size(self) -> int:
        return len(self.__exercise)

    def find_new_primary_key(self):
        maxid: int = self.__exercise[0].id_exercise
        for i in range(len(self.__exercise)):
            if maxid < self.__exercise[i].id_exercise:
                maxid = self.__exercise[i].id_exercise
        return maxid + 1
