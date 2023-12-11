import customtkinter as ctk


class Application:
    def __init__(self, name, dimensions):
        app = ctk.CTk()
        app.title(name)
        app.geometry(dimensions)
        app.mainloop()
        print("Initialised!")
