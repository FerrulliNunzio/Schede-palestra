import tkinter as tk
from tkinter import ttk

from Settings.Setting import Setting
from db.table.tables import WorkoutExercisesTable, ExerciseTable

def ins_tab(input_string: str, tab_position: int):
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
    return input_string

"""
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


"""


class WorkoutScreen:

    def __init__(self, workout: str, split: str):
        self.root = tk.Tk()
        self.root.title("Impostazioni Globali")
        self.root.geometry(Setting.screen_size)

        # Frame principale
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Inizia il workout", fg="white", bg="black", font=("Calibri", 15)).pack()
        workout_exercise: list = []
        top: str = ''
        top_exercise: str = '|Esercizio'
        top_series: str = 'Serie'
        top_reps: str = 'Reps'
        top = ins_tab(top_exercise, 50) + ins_tab(top_series, 5) + ins_tab(top_reps, 15)
        """workout_exercise.append('+------------------------------------------------------------------------+')
        workout_exercise.append(top)
        workout_exercise.append('+------------------------------------------------------------------------+')
"""
        exercise_name: str = ''
        series: str = ''
        reps: str = ''
        for item in WorkoutExercisesTable.get():  # type: StrWorkoutExercises
            if item.workout_id.__str__() == workout[1] and item.id_training_plan.__str__() == split[1]:
                string: str = ''
                for exercise in ExerciseTable.get():  # type: StrExercise
                    if exercise.id_exercise == item.exercise_id:
                        exercise_name = exercise.name
                        break
                string += ins_tab(exercise_name, 50) + ins_tab(item.sets.__str__(), 5) + item.reps #ins_tab(item.reps, 15)
                workout_exercise.append(string)
                #workout_exercise.append('+------------------------------------------------------------------------+')

        # Treeview (tabella)
        tree = ttk.Treeview(frame, columns=("Esercizio", "Serie", "Reps"), show="headings")

        # intestazioni
        tree.heading("Esercizio", text="Esercizio")
        tree.heading("Serie", text="Serie")
        tree.heading("Reps", text="Reps")

        # larghezza colonne
        tree.column("Esercizio", width=400)
        tree.column("Serie", width=80, anchor="center")
        tree.column("Reps", width=120, anchor="center")

        # inserimento righe
        for riga in workout_exercise:
            esercizio, serie, reps = riga.split('|')
            tree.insert("", "end", values=(esercizio, serie, reps))

        # scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)

        tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        """text: str = ''
        for item in workout_exercise:
            text += item + '\n'"""



