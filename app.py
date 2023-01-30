# import customtkinter as ctk
# 
# class App(ctk.CTk):
    # def __init__(self):
        # super().__init__()
        # self.title("LoRA Dataset Manager")
        # self.geometry("800x600")
# 
# if __name__ == "__main__":
    # app = App()
    # app.mainloop()

from src.model.dl_from_danbooru import dl_from_danbooru_id

# Ask the user for the ID
id = input("Enter the ID of the image to download: ")
# Ask the user for the output directory
output_dir = input("Enter the output directory: ")
# Ask the user for the custom name
custom_name = input("Enter the custom name (leave empty for default): ")
# Ask the user if they want to download the captions
dl_captions = input("Download captions? (y/n): ") == "y"

# Download the image
dl_from_danbooru_id(id, output_dir, custom_name, dl_captions)