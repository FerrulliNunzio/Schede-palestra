import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import openpyxl

from openpyxl.styles import PatternFill, Font

import pandas as pd
from pandas import DataFrame
import os

from Settings.Setting import Setting




class SettingScreen(tk.Tk):
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
            bg="#2b2b2b",
            fg="white",
            font=("Arial", 16, "bold")
        )
        title.pack(side="left", padx=20)

        btn_home = tk.Button(frame, text="Home", command=self.__home)
        btn_home.pack(side="right", padx=10, pady=10)

        # ===== MAIN CONTAINER =====
        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        # ===== SIDEBAR =====
        sidebar = tk.Frame(container, bg="#333333", width=200)
        sidebar.pack(side="left", fill="y")

        menu_items: list = ["Schede", "Esercizi", "Home"]
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

        self.dimensioni = [
            "800x600",
            "1024x768",
            "1280x720",
            "1366x768",
            "1600x900",
            "1920x1080"
        ]

        frame_dim =  tk.Frame(container)

        tk.Label(
            frame_dim,
            text="Dimensioni",
            bg="#2b2b2b",
            fg="white",
        ).pack(side="left", padx=20)

        self.combobox = ttk.Combobox(frame_dim, values=self.dimensioni, state="readonly")
        self.combobox.current(0)
        #self.combobox.pack(padx=0, pady=270)
        self.combobox.pack(padx=0)

        #self.combobox.bind("<<ComboboxSelected>>", self.on_select())

        tk.Button(
            frame,
            text="Applica modifiche.",
            command=self.on_select
        ).pack(pady=5)

        self.mainloop()

    def on_select(self):
        Setting.change_screen_size(self.combobox.get())
        self.root.destroy()
        SettingScreen()

    def __home(self):
        pass
