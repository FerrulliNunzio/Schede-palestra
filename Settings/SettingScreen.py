import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox
import openpyxl

from openpyxl.styles import PatternFill, Font

import pandas as pd
from pandas import DataFrame
import os

from Settings.Setting import Setting




class SettingScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Impostazioni Globali")
        self.root.geometry(Setting.screen_size)

        # Frame principale
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True)

        # Titolo
        titolo = tk.Label(
            frame,
            text="Impostazioni",
            font=("Arial", 14, "bold")
        )
        titolo.pack(pady=(0, 20))

        # Dimensioni preimpostate
        self.dimensioni = [
            "800x600",
            "1024x768",
            "1280x720",
            "1366x768",
            "1600x900",
            "1920x1080"
        ]

        self.combobox = ttk.Combobox(self.root, values=self.dimensioni, state="readonly")
        self.combobox.current(0)
        self.combobox.pack(padx=50, pady=270)

        #self.combobox.bind("<<ComboboxSelected>>", self.on_select())

        Setting.change_screen_size(self.combobox.get())

        self.root.mainloop()

    def on_select(self):
        Setting.change_screen_size(self.combobox.get())
