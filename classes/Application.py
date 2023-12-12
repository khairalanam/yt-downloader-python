import customtkinter as ctk
from types import FunctionType
from tkinter import messagebox


class Application:
    def __init__(self, name: str, dimensions: str):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.app = ctk.CTk()
        self.app.title(name)
        self.app.geometry(dimensions)
        print("Initialised!")

    def run_app(self):
        self.app.mainloop()

    def add_label(self, name: str, x: int = 20, y: int = 20):
        main_label = ctk.CTkLabel(
            self.app, text=name, font=("Helvetica", 20, "bold"))
        main_label.pack(padx=x, pady=y)

    def add_entry(self, width: int, height: int, x: int = 20, y: int = 20):
        entry_var = ctk.StringVar()
        entry_box = ctk.CTkEntry(
            self.app, textvariable=entry_var, width=width, height=height)
        entry_box.pack(padx=x, pady=y)
        return entry_var

    def add_button(self, name: str, width: int, height: int, callback: FunctionType, params=None, x: int = 20, y: int = 20):
        main_button = ctk.CTkButton(
            self.app, text=name, command=lambda: callback(params), font=("Helvetica", 20, "bold"), width=width, height=height)
        main_button.pack(padx=x, pady=y)

    @staticmethod
    def show_error(title, desc):
        messagebox.showerror(title, desc)

    @staticmethod
    def show_info(title, desc):
        messagebox.showinfo(title, desc)
