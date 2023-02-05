import customtkinter as ctk

class App(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add a new image to the dataset")
        self.geometry("600x300")
        self._setup_ui()

    def _setup_ui(self):
        pass