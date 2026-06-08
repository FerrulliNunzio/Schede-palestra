# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
import os

from Settings.Setting import Setting
from Settings.SettingScreen import SettingScreen
from Workout import Workout
from db.structure.StrExercise import StrExercise
from db.structure.StrTrainingPlans import StrTrainingPlans
from db.structure.StrUser import StrUser
from db.structure.StrWorkout import StrWorkout
from db.structure.StrWorkoutExercises import StrWorkoutExercises
from db.table.Exercise import Exercise
from db.table.TrainingPlans import TrainingPlans
# from db.table.tables import UsersTable, TrainingPlansTable
from db.table.tables import TrainingPlansTable, WorkoutTable, WorkoutExercisesTable, ExerciseTable
from file_management.FileManager import FileManager

import tkinter as tk

def select_training_plans() -> list:
    training_plans: list = []
    for item in TrainingPlansTable.get():  # type: StrTrainingPlans
        training_plans.append('(' + item.TrainingPlansId.__str__() + ') ' + item.Name)
    return training_plans


def select_workout(training_plans_id: str):
    workout: list = []
    for item in WorkoutTable.get():  # type: StrWorkout
        if item.id_workout.__str__() == training_plans_id:
            workout.append('(' + item.id_training_plan.__str__() + ') ' + item.name)
    return workout

"""def ins_tab(input_string: str, tab_position: int):
    if tab_position == 50:
        match len(input_string):
            case 1:
                input_string += '                                                 |'
            case 2:
                input_string += '                                                |'
            case 3:
                input_string += '                                               |'
            case 4:
                input_string += '                                              |'
            case 5:
                input_string += '                                             |'
            case 6:
                input_string += '                                            |'
            case 7:
                input_string += '                                           |'
            case 8:
                input_string += '                                          |'
            case 9:
                input_string += '                                         |'
            case 10:
                input_string += '                                         |'
            case 11:
                input_string += '                                       |'
            case 12:
                input_string += '                                      |'
            case 13:
                input_string += '                                     |'
            case 14:
                input_string += '                                    |'
            case 15:
                input_string += '                                   |'
            case 16:
                input_string += '                                  |'
            case 17:
                input_string += '                                 |'
            case 18:
                input_string += '                                |'
            case 19:
                input_string += '                               |'
            case 20:
                input_string += '                              |'
            case 21:
                input_string += '                             |'
            case 22:
                input_string += '                            |'
            case 23:
                input_string += '                           |'
            case 24:
                input_string += '                          |'
            case 25:
                input_string += '                         |'
            case 26:
                input_string += '                        |'
            case 27:
                input_string += '                       |'
            case 28:
                input_string += '                      |'
            case 29:
                input_string += '                     |'
            case 30:
                input_string += '                    |'
            case 31:
                input_string += '                   |'
            case 32:
                input_string += '                  |'
            case 33:
                input_string += '                 |'
            case 34:
                input_string += '                |'
            case 35:
                input_string += '               |'
            case 36:
                input_string += '              |'
            case 37:
                input_string += '             |'
            case 38:
                input_string += '            |'
            case 39:
                input_string += '           |'
            case 40:
                input_string += '          |'
            case 41:
                input_string += '         |'
            case 42:
                input_string += '        |'
            case 43:
                input_string += '       |'
            case 44:
                input_string += '      |'
            case 45:
                input_string += '     |'
            case 46:
                input_string += '    |'
            case 47:
                input_string += '   |'
            case 48:
                input_string += '  |'
            case 49:
                input_string += ' |'
            case 50:
                input_string += '|'

    if tab_position == 5:
        match len(input_string):
            case 1:
                input_string += '    |'
            case 2:
                input_string += '   |'
            case 3:
                input_string += '  |'
            case 4:
                input_string += ' |'
            case 5:
                input_string += '|'

    if tab_position == 15:
        match len(input_string):
            case 1:
                input_string += '              |'
            case 2:
                input_string += '             |'
            case 3:
                input_string += '            |'
            case 4:
                input_string += '           |'
            case 5:
                input_string += '          |'
            case 6:
                input_string += '         |'
            case 7:
                input_string += '        |'
            case 8:
                input_string += '       |'
            case 9:
                input_string += '      |'
            case 10:
                input_string += '     |'
            case 11:
                input_string += '    |'
            case 12:
                input_string += '   |'
            case 13:
                input_string += '  |'
            case 14:
                input_string += ' |'
            case 15:
                input_string += '|'
    return input_string"""



if __name__ == '__main__':

    # TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="Multifrequenza Intermedio",goal="Ipertrofia", duration=8))
    """TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="1",goal="Ipertrofia", duration=8))
    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=4, name="2",goal="Ipertrofia", duration=8))
    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="3",goal="Ipertrofia", duration=8))
    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="4",goal="Ipertrofia", duration=8))
    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="5",goal="Ipertrofia", duration=8))"""

    """WorkoutTable.add_workout(StrWorkout(id_workout=1, id_training_plan=1, name="Push", day_week="Lunedi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=1, id_training_plan=2, name="Pull", day_week="Mercoledi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=1, id_training_plan=3, name="Total", day_week="Venerdi"))

    ExerciseTable.add_exercise(StrExercise(id_exercise = 1, name = "PANCA PIANA BILANCIERE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 2, name = "INCLINE CHEST PRESS"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 3, name = "CROCI AI CAVI BASSI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 4, name = "SHOULDER PRESS"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 5, name = "ALZATE LATERALI AI CAVI INCROCIATI IN PIEDI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 6, name = "ESTENSIONI SOPRA LA TESTA FUNE CAVO BASSO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 7, name = "PUSH DOWN AL CAVO ALTRO CON SBARRA"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 8, name = "LEG PRESS ORIZZONTALE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 9, name = "CALF ALLA LEG PRESS 45°"))
    ExerciseTable.add_exercise(StrExercise(id_exercise = 10, name = "CALF IN PIEDI A CORPO LIBERO"))

    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=1, sets=4, reps='6', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=2, sets=3, reps='10', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=3, sets=3, reps='12', weight=10))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=4, sets=4, reps='10-8-6-4', weight=10))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=5, sets=3, reps='10-12', weight=8))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=6, sets=4, reps='8-10', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=7, sets=4, reps='8-10', weight=15))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=8, sets=4, reps='8+MAX', weight=10))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=9, sets=4, reps='12-15', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, exercise_id=10, sets=4, reps='MAX', weight=0))
"""
    """close: bool = False
    option: str = ''

    while not close:
        match option:
            case '':
                print("Seleziona un opzione:\n"
                      "(1) Selezionare allenamento\n"
                      "(2) Termina applicazione\n")
                option = input("Inserire opzione [1-2] -> ")
            case '1':
                print("Seleziona una scheda")
                training_plans = select_training_plans()
                for item in training_plans:
                    print(item)
                print('(' + (len(training_plans) + 1).__str__() + ') Indietro\n')
                option = input(f"Seleziona una scheda [1:{len(training_plans) + 1}] -> ")

                if option == '2':
                    option = ''
                else:
                    workout = select_workout(option)
                    print("Selezione un allenamento\n")
                    for item in workout:
                        print(item)
                    print('(' + (len(workout) + 1).__str__() + ') Indietro\n')
                    option = input(f"Seleziona un allenamento [1:{len(workout) + 1}] -> ")

                    if option == (len(workout) + 1).__str__():
                        option = ''
                    else:
                        workout_exercise: list = []
                        top: str = ''
                        top_exercise: str = '|Esercizio'
                        top_series: str = 'Serie'
                        top_reps: str = 'Reps'
                        top = ins_tab(top_exercise, 50) + ins_tab(top_series, 5) + ins_tab(top_reps, 15)
                        workout_exercise.append('+------------------------------------------------------------------------+')
                        workout_exercise.append(top)
                        workout_exercise.append('+------------------------------------------------------------------------+')

                        exercise_name: str = ''
                        series: str = ''
                        reps: str = ''
                        for item in WorkoutExercisesTable.get():  # type: StrWorkoutExercises
                            if item.workout_id.__str__() == option:
                                string: str = '|'
                                for exercise in ExerciseTable.get():  # type: StrExercise
                                    if exercise.id_exercise == item.exercise_id:
                                        exercise_name = exercise.name
                                        break
                                string += ins_tab(exercise_name, 50) + ins_tab(item.sets.__str__(), 5) + ins_tab(item.reps, 15)
                                workout_exercise.append(string)
                                workout_exercise.append('+------------------------------------------------------------------------+')
                        for item in workout_exercise:
                            print(item)
            case '2':
                close = True
                break"""

    if not os.path.exists(r"C:\SchedePalestra"):
        FileManager.directory_create(r"C:\SchedePalestra")

    setting: Setting = Setting()

    SettingScreen()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
