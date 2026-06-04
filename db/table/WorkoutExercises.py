import pandas as pd

from db.structure.StrWorkoutExercises import StrWorkoutExercises
from db.table.TableOperation import TableOperation


class WorkoutExercises(TableOperation):

    def __init__(self):
        self.__workout_exercises: list = []
        try:
            workout = pd.read_csv("WorkoutExercises.csv")
            lst = workout.values.tolist()
            for item in lst:
                self.__workout_exercises.append(StrWorkoutExercises(item[0], item[1], item[2], item[3], item[4]))
        except FileNotFoundError:
            self.__training_plans = []

    def get(self):
        return self.__workout_exercises

    def add_workout_exercise(self, workout_exercise: StrWorkoutExercises):
        self.__workout_exercises.append(workout_exercise)
        to_save: list = []
        to_save.append([
            'workout_id',
            'exercise_id',
            'sets',
            'reps',
            'weight',
        ])
        for item in self.__workout_exercises:
            to_save.append([item.workout_id,
                            item.exercise_id,
                            item.sets,
                            item.reps,
                            item.weight,
                            ])
        self.save_table("WorkoutExercises.csv", to_save)

    def size(self) -> int:
        return len(self.__workout_exercises)

    def find_new_primary_key(self):
        maxid: int = self.__workout_exercises[0].workout_exercise_id
        for i in range(len(self.__workout_exercises)):
            if maxid < self.__workout_exercises[i].workout_exercise_id:
                maxid = self.__workout_exercises[i].workout_exercise_id
        return maxid + 1
