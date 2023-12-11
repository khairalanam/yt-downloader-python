import customtkinter as ctk


class Application:
    def __init__(self, name, dimensions):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        self.app = ctk.CTk()
        self.app.title(name)
        self.app.geometry(dimensions)
        print("Initialised!")

    def run_app(self):
        self.app.mainloop()

    def add_label(self, name, x=20, y=20):
        main_label = ctk.CTkLabel(
            self.app, text=name, font=("Helvetica", 20, "bold"))
        main_label.pack(padx=x, pady=y)

    def add_entry(self, width, height, x=20, y=20):
        entry_var = ctk.StringVar()
        entry_box = ctk.CTkEntry(
            self.app, textvariable=entry_var, width=width, height=height)
        entry_box.pack(padx=x, pady=y)
        return entry_var

    def add_button(self, name, width, height, callback, params=None, x=20, y=20):
        main_button = ctk.CTkButton(
            self.app, text=name, command=lambda: callback(params), font=("Helvetica", 20, "bold"), width=width, height=height)
        main_button.pack(padx=x, pady=y)
