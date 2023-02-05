import customtkinter as ctk
import tkinter as tk

class DatasetViewer(ctk.CTkToplevel):
    def __init__(self, parent, dataset_path):
        super().__init__(parent)
        self.title("Dataset Viewer")
        self.geometry("800x600")

        self.dataset_path = dataset_path

        self.panel = tk.PanedWindow(self, orient=tk.HORIZONTAL, bd=0)
        self.panel.pack(fill=tk.BOTH, expand=True)

        self._setup_navigation_frame()
        self._setup_image_frame()
        self._setup_captions_frame()

    def _setup_navigation_frame(self):
        self.first_frame = ctk.CTkFrame(self.panel, corner_radius=0, fg_color="red", border_width=1)
        self.panel.add(self.first_frame)

    def _setup_image_frame(self):
        self.second_frame = ctk.CTkFrame(self.panel, corner_radius=0, fg_color="blue", border_width=1)
        self.panel.add(self.second_frame)

        self.btn = ctk.CTkButton(self.second_frame, text="test")
        self.btn.pack(side=tk.LEFT, fill=tk.Y)

    def _setup_captions_frame(self):
        self.third_frame = ctk.CTkFrame(self.panel, corner_radius=0, fg_color="green", border_width=1)
        self.panel.add(self.third_frame)

        label = ctk.CTkLabel(self.third_frame, text="test\nabcd")
        label.pack()

        btn = ctk.CTkButton(self.third_frame, text="click me")
        btn.pack()