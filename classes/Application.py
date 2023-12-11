import customtkinter as ctk


class Application:
    def __init__(self, name, dimensions):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.app = ctk.CTk()
        self.app.title(name)
        self.app.geometry(dimensions)
        self.app.mainloop()
        print("Initialised!")

    def add_label(self, name, x, y):
        main_label = ctk.CTkLabel(self.app, text=name)
        main_label.pack(padx=x, pady=y)

    def add_entry(self, text, x, y):
        entry_var = ctk.StringVar()
        entry_box = ctk.CTkEntry(self.app, text=text, textvariable=entry_var)
        entry_box.pack(padx=x, pady=y)
        return entry_var

    def add_button(self, name, x, y, callback):
        main_button = ctk.CTkButton(self.app, text=name, command=callback)
        main_button.pack(padx=x, pady=y)
