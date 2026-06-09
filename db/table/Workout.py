from db.structure.StrWorkout import StrWorkout
from db.table.TableOperation import TableOperation
import pandas as pd

class Workout(TableOperation):

    def __init__(self):
        self.__workout: list = []
        try:
            workout = pd.read_csv(r"C:\SchedePalestra\Workout.csv")
            lst = workout.values.tolist()
            for item in lst:
                self.__workout.append(StrWorkout(item[0], item[1], item[2], item[3]))
        except FileNotFoundError:
            self.__training_plans = []

    def get(self):
        return self.__workout

    def add_workout(self, workout: StrWorkout):
        if len(self.__workout) <= 0:
            workout.id_workout = 1
            self.__workout.append(workout)
            to_save: list = []
            to_save.append([
                'id_workout',
                'id_training_plan',
                'name',
                'day_week',
            ])
            for item in self.__workout:
                to_save.append([item.id_workout,
                                item.id_training_plan,
                                item.name,
                                item.day_week,
                                ])
            self.save_table(r"C:\SchedePalestra\Workout.csv", to_save)
        else:
            if workout.id_workout == 0:
                workout.id_workout = self.find_new_primary_key()
            self.__workout.append(workout)
            to_save: list = []
            to_save.append([
                'id_workout',
                'id_training_plan',
                'name',
                'day_week',
            ])
            for item in self.__workout:
                to_save.append([item.id_workout,
                                item.id_training_plan,
                                item.name,
                                item.day_week,
                                ])
            self.save_table(r"C:\SchedePalestra\Workout.csv", to_save)


    def size(self) -> int:
        return len(self.__workout)

    def find_new_primary_key(self):
        maxid: str = self.__workout[0].id_workout
        for i in range(len(self.__workout)):
            if maxid < self.__workout[i].id_workout:
                maxid = self.__workout[i].id_workout
        return maxid + 1
