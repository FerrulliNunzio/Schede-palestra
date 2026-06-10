import tkinter as tk
from tkinter import ttk

from Settings.Setting import Setting
from Settings.SettingScreen import SettingScreen
from screens.SplitScreen import SplitScreen
from db.table.tables import TrainingPlansTable

def select_training_plans() -> list:
    training_plans: list = []
    for item in TrainingPlansTable.get():  # type: StrTrainingPlans
        training_plans.append('(' + item.TrainingPlansId.__str__() + ') ' + item.Name)
    return training_plans

class MainScreen(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("GymTonic")
        self.geometry(Setting.screen_size)

        self.configure(bg="#1e1e1e")

        # Frame principale
        frame = tk.Frame(self, bg="#2b2b2b")
        frame.pack(side="top", fill="x")

        title = tk.Label(
            frame,
            text="GymTonic",
            bg = "#2b2b2b",
            fg = "white",
            font = ("Arial", 16, "bold")
        )
        title.pack(side="left", padx=20)

        btn_setting = tk.Button(frame, text="Impostazioni", command=self.__setting)
        btn_setting.pack(side="right", padx=10, pady=10)

        # ===== MAIN CONTAINER =====
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # ===== SIDEBAR =====
        sidebar = tk.Frame(container, bg="#333333", width=200)
        sidebar.pack(side="left", fill="y")

        menu_items: list = ["Schede", "Esercizi", "Impostazioni"]
        for item in menu_items:
            tk.Button(
                sidebar,
                text=item,
                bg="#444444",
                fg="white",
                relief="flat"
            ).pack(fill="x", padx=10, pady=10)

        # ===== MAIN CONTENT =====
        main_area = tk.Frame(container, bg="#f0f0f0")
        main_area.pack(side="left", fill="both", expand=True)

        tk.Label(
            main_area,
            text="Lista Schede Allenamento",
            font=("Arial", 14)
        ).pack(pady=10)

        # Lista schede (placeholder)
        self.listbox = tk.Listbox(main_area)
        self.listbox.pack(fill="both", expand=True, padx=20, pady=10)

        training_plans = select_training_plans()

        for i in training_plans:
            self.listbox.insert("end", f"{i}")

        tk.Button(
            main_area,
            text="Apri scheda",
            command=self.__open,
            bg="#444444",
            fg="white",
            relief="flat"
        ).pack(fill="x", padx=10, pady=10)

        self.mainloop()

    def __open(self):
        indici = self.listbox.curselection()
        for i in indici:
            workout = self.listbox.get(i)
        self.destroy()
        SplitScreen(workout)

    def __setting(self):
        self.destroy()
        SettingScreen()



