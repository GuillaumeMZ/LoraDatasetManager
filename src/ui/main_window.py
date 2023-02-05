import customtkinter as ctk
from .dataset_viewer import DatasetViewer

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoRA Dataset Manager")
        self.geometry("600x300")

        self.dataset_viewer = DatasetViewer(self, "test")