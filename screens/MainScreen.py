import tkinter as tk
from tkinter import ttk

from Settings.Setting import Setting
from screens.SplitScreen import SplitScreen
from db.table.tables import TrainingPlansTable

def select_training_plans() -> list:
    training_plans: list = []
    for item in TrainingPlansTable.get():  # type: StrTrainingPlans
        training_plans.append('(' + item.TrainingPlansId.__str__() + ') ' + item.Name)
    return training_plans

class MainScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Impostazioni Globali")
        self.root.geometry(Setting.screen_size)

        # Frame principale
        frame = tk.Frame(self.root, bg="white")
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="I tuoi workout", fg="red", bg="white", font=("Calibri", 15)).pack()
        #tk.Label(frame, text="I tuoi workout", fg="red", bg="white", font=("Calibri", 15)).grid(row=0, column=0, sticky="w")

        training_plans = select_training_plans()
        self.combobox = ttk.Combobox(frame, values=training_plans, state="readonly", width=100)
        self.combobox.current(0)
        self.combobox.pack(padx=0)

        tk.Button(
            frame,
            text="Apri",
            command=self.__open
        ).pack(pady=5)

        self.root.mainloop()

    def __open(self):
        workout = self.combobox.get()
        self.root.destroy()
        SplitScreen(workout)



