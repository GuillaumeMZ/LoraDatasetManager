import customtkinter as ctk


class App(ctk.CTkToplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Add a new image to the dataset")
        self.geometry("600x300")
        self._setup_ui()

    def _setup_ui(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self._image_url = ctk.CTkEntry(self, placeholder_text="Image URL", justify="center")
        self._image_url.grid(row=0, column=0, sticky="nwe", padx=10, pady=10)

        self._download_button = ctk.CTkButton(self, text="Add image")
        self._download_button.grid(row=1, column=0, sticky="swe", padx=10, pady=10)