import tkinter as tk

class CustomPanedWindow(tk.PanedWindow):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._current_width = self.winfo_width()
        
        self._sashes_count = 0
        self._sashes_pos = []

        self.bind("<Configure>", self._on_resize_panel)

    def _on_resize_panel(self, resize_event):
        sashes_coords = [self.sash_coord(i)[0] for i in range(2)]
        new_sashes_coords = [int(coord/self._current_width * resize_event.width) for coord in sashes_coords]

        for i, coord in enumerate(new_sashes_coords):
            self.sash_place(i, coord, 0)

        self._current_width = resize_event.width

    # Overriding these methods is necessary to keep track of the number of sashes
    def add(self, child=None, **kwargs):
        super().add(child, **kwargs)
        self._sashes_count += 1

    def forget(self, child):
        super().forget(child)
        self._sashes_count -= 1

    def remove(self, child):
        super().remove(child)
        self._sashes_count -= 1