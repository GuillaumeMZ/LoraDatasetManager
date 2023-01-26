import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("LoRA Dataset Manager")
        self.geometry("800x600")

if __name__ == "__main__":
    app = App()
    app.mainloop()