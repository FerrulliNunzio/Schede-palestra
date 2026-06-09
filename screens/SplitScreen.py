import tkinter as tk
from tkinter import ttk

from Settings.Setting import Setting
from db.table.tables import WorkoutTable
from screens.WorkoutScreen import WorkoutScreen


def select_workout(training_plans_id: str):
    workout: list = []
    for item in WorkoutTable.get():  # type: StrWorkout
        if item.id_workout.__str__() == training_plans_id:
            workout.append('(' + item.id_training_plan.__str__() + ') ' + item.name)
    return workout

class SplitScreen:
    def __init__(self, workout: str):
        self.__workout = workout
        self.root = tk.Tk()
        self.root.title("Impostazioni Globali")
        self.root.geometry(Setting.screen_size)

        # Frame principale
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text=workout[4:], fg="red", bg="white", font=("Calibri", 15)).pack()

        split = select_workout(workout[1])

        self.combobox = ttk.Combobox(frame, values=split, state="readonly", width=100)
        self.combobox.current(0)
        self.combobox.pack(padx=0)

        tk.Button(
            frame,
            text="Apri workout",
            command=self.__open_workout
        ).pack(pady=5)

        self.root.mainloop()

    def __open_workout(self):
        split = self.combobox.get()
        self.root.destroy()
        WorkoutScreen(self.__workout, split)

