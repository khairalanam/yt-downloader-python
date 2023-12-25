import customtkinter as ctk
from types import FunctionType
from tkinter import messagebox
from functools import partial
from PIL import Image
import urllib.request
from io import BytesIO
import time


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

    def add_label(self, name: str, x: int = 20, y: int = 10):
        main_label = ctk.CTkLabel(
            self.app, text=name, font=("Helvetica", 15, "bold"))
        main_label.pack(padx=x, pady=y)
        return main_label

    def add_entry(self, width: int, height: int, x: int = 20, y: int = 10):
        entry_var = ctk.StringVar()
        entry_box = ctk.CTkEntry(
            self.app, textvariable=entry_var, width=width, height=height)
        entry_box.pack(padx=x, pady=y)
        return entry_var

    def add_button(self, name: str, width: int, height: int, func: FunctionType, params, x: int = 20, y: int = 10):
        main_button = ctk.CTkButton(
            self.app, text=name, command=partial(func, params), font=("Helvetica", 15, "bold"), width=width, height=height)
        main_button.pack(padx=x, pady=y)

    @staticmethod
    def show_error(title, desc):
        messagebox.showerror(title, desc)

    @staticmethod
    def show_info(title, desc):
        messagebox.showinfo(title, desc)

    def add_image(self, src, x: int = 10, y: int = 10, dimensions: (int, int) = (60, 80)):
        main_image = ctk.CTkImage(dark_image=Image.open(src), size=dimensions)
        image_label = ctk.CTkLabel(self.app, image=main_image, text="")
        image_label.pack(padx=x, pady=y)
        return image_label

    @staticmethod
    def show_image_from_url(image_url: str):
        with urllib.request.urlopen(image_url) as url_response:
            img_data = url_response.read()

        return BytesIO(img_data)

    def add_progress_bar(self, x=20, y=10, w=400):
        progress_bar = ctk.CTkProgressBar(self.app, width=w)
        progress_bar.set(0)
        progress_bar.pack(padx=x, pady=y)
        return progress_bar
