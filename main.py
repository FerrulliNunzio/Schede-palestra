# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Press the green button in the gutter to run the script.
import os

from Settings.SettingScreen import SettingScreen
from db.structure.StrExercise import StrExercise
from db.structure.StrTrainingPlans import StrTrainingPlans
from db.structure.StrWorkout import StrWorkout
from db.structure.StrWorkoutExercises import StrWorkoutExercises
from db.table.tables import TrainingPlansTable, WorkoutTable, ExerciseTable, WorkoutExercisesTable
from screens.MainScreen import MainScreen
from Settings.Setting import Setting
# from db.table.tables import UsersTable, TrainingPlansTable
from file_management.FileManager import FileManager

"""    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="3",goal="Ipertrofia", duration=8))
    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="4",goal="Ipertrofia", duration=8))
    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="5",goal="Ipertrofia", duration=8))"""


if __name__ == '__main__':

    if not os.path.exists(r"C:\SchedePalestra"):
        FileManager.directory_create(r"C:\SchedePalestra")

# Prima scheda

    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="Multifrequenza Intermedio", goal="Ipertrofia", duration=8))

    WorkoutTable.add_workout(StrWorkout(id_workout=1, id_training_plan=1, name="Push", day_week="Lunedi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=1, id_training_plan=2, name="Pull", day_week="Mercoledi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=1, id_training_plan=3, name="Total", day_week="Venerdi"))

    ExerciseTable.add_exercise(StrExercise(id_exercise=1, name="PANCA PIANA BILANCIERE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=2, name="INCLINE CHEST PRESS"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=3, name="CROCI AI CAVI BASSI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=4, name="SHOULDER PRESS"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=5, name="ALZATE LATERALI AI CAVI INCROCIATI IN PIEDI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=6, name="ESTENSIONI SOPRA LA TESTA FUNE CAVO BASSO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=7, name="PUSH DOWN AL CAVO ALTRO CON SBARRA"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=8, name="LEG PRESS ORIZZONTALE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=9, name="CALF ALLA LEG PRESS 45°"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=10, name="CALF IN PIEDI A CORPO LIBERO"))

    ExerciseTable.add_exercise(StrExercise(id_exercise=11, name="STACCO DA TERRA"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=12, name="HYPEREXTENSION"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=13, name="LEG CURL DISTESO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=14, name="TRAZIONI ALLA SBARRA"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=15, name="REMATORE T-BAR SINGOLO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=16, name="PULL DOWN AL CAVO ALTO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=17, name="FACE PULL AL CAVO ALTO CON FUNE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=18, name="CURL CON MANUBRI PANCA 45°"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=19, name="SPIDER CURL CON MANUBRI SU PANCA 45°"))

    ExerciseTable.add_exercise(StrExercise(id_exercise=20, name="SQUAT CON BILANCIERE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=21, name="AFFONDI CAMMINATI CON MANUBRI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=22, name="LEG EXTENSION"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=23, name="CALF MACHINE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=24, name="STACCO RUMENO BILANCIERE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=25, name="DISTENSIONI MANUBRI PANCA PIANA"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=26, name="LAT MACHINE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=27, name="FRENCH PRESS CON BILANCIERE SABOMATO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=28, name="CURL IN PIEDI CON BILANCIERE SAGOMATO PRESA LARGA"))

    ExerciseTable.add_exercise(StrExercise(id_exercise=29, name="CALF IN PIEDI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=30, name="LEG CURL O MEZZI STACCHI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=31, name="PULLEY"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=32, name="CROCI PANCA INCLINATA 40° MANUBRI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=33, name="FLESSIONI GAMBRE RIALZATE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=34, name="PUSH DOWN"))

    ExerciseTable.add_exercise(StrExercise(id_exercise=35, name="ALZATE LATERALI MANUBRI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=36, name="PANCA INCLINATA 50° MANUBRI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=37, name="PULL OVER MANUBRIO SDRAIATO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=38, name="CURL MANUBRI A MARTELLO SEDUTO"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=39, name="CRUNCH INVERSI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=40, name="LEG PRESS INCLINATA O ORIZZONTALE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=41, name="AFFONDI CON MANUBRI ALTERNATI"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=42, name="DIP ALLE PARALLELE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=43, name="TIRATE AL PETTO BILANCIERE"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=44, name="PANCA SCOTT BILANCIERE PRESA INVERSA"))
    ExerciseTable.add_exercise(StrExercise(id_exercise=45, name="CRUNCH DOPPIO"))

    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=1, sets=4, reps='6', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=2, sets=3, reps='10', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=3, sets=3, reps='12', weight=10))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=4, sets=4, reps='10-8-6-4', weight=10))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=5, sets=3, reps='10-12', weight=8))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=6, sets=4, reps='8-10', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=7, sets=4, reps='8-10', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=8, sets=4, reps='8+MAX', weight=10))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=9, sets=4, reps='12-15', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=1, exercise_id=10, sets=4, reps='12-15', weight=20))

    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=11, sets=4, reps='4-6', weight=25))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=12, sets=3, reps='8-10', weight=0))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=13, sets=3, reps='10-12', weight=35))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=14, sets=4, reps='MAX', weight=0))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=15, sets=4, reps='10-8-6-4', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=16, sets=3, reps='10-12', weight=30))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=17, sets=4, reps='8+MAX', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=18, sets=4, reps='8-10', weight=10))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=2, exercise_id=19, sets=4, reps='8-10', weight=10))

    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=20, sets=4, reps='4-6', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=21, sets=3, reps='16 PASSI', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=22, sets=3, reps='10-12', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=23, sets=4, reps='8+MAX', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=24, sets=4, reps='8+MAX', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=25, sets=4, reps='10-8-6-4', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=26, sets=4, reps='8+MAX', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=27, sets=4, reps='10-12', weight=20))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=1, id_training_plan=3, exercise_id=28, sets=4, reps='10-12', weight=20))

# Seconda scheda

    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=3, name="1", goal="Ipertrofia", duration=8))

    WorkoutTable.add_workout(StrWorkout(id_workout=2, id_training_plan=1, name="Lunedì", day_week="Lunedi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=2, id_training_plan=2, name="Mercoledì", day_week="Mercoledi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=2, id_training_plan=3, name="Venerdì", day_week="Venerdi"))

    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=29, sets=3, reps='10-15', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=22, sets=3, reps='12-10-8', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=20, sets=3, reps='8-10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=30, sets=3, reps='8-10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=31, sets=3, reps='12-10-8', weight=22))
    WorkoutExercisesTable.add_workout_exercise( StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=32, sets=3, reps='8-10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=33, sets=2, reps='MAX', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=27, sets=3, reps='12-10-8', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=1, exercise_id=34, sets=2, reps='8-10', weight=22))

    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=26, sets=3, reps='8-12', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=35, sets=2, reps='10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=36, sets=3, reps='8-12', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=1, sets=3, reps='8', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=37, sets=2, reps='12', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=38, sets=2, reps='12-10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=28, sets=3, reps='8-10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=2, exercise_id=29, sets=3, reps='20-25', weight=22))

    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=40, sets=3, reps='12-10-8', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=41, sets=3, reps='8', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=11, sets=3, reps='10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=14, sets=3, reps='8-12', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=42, sets=3, reps='8-10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=4, sets=2, reps='10-8', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=43, sets=2, reps='12-10', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=44, sets=3, reps='10-12', weight=22))
    WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=2, id_training_plan=3, exercise_id=45, sets=3, reps='25-30', weight=22))

#Terza scheda

    TrainingPlansTable.add_training_plans(StrTrainingPlans(user_id=1, workout=4, name="2", goal="Ipertrofia", duration=8))

    WorkoutTable.add_workout(StrWorkout(id_workout=3, id_training_plan=1, name="Lunedì", day_week="Lunedi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=3, id_training_plan=2, name="Mercoledì", day_week="Mercoledi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=3, id_training_plan=3, name="Venerdì", day_week="Venerdi"))
    WorkoutTable.add_workout(StrWorkout(id_workout=3, id_training_plan=4, name="Sabato", day_week="Sabato"))

    #WorkoutExercisesTable.add_workout_exercise(StrWorkoutExercises(workout_id=4, id_training_plan=1, exercise_id=, sets=, reps='', weight=22))


    setting: Setting = Setting()

    # SettingScreen()

    MainScreen()

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/

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
