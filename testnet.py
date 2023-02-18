# program testujący nauczoną sieć
from tkinter import ttk
from tkinter import filedialog

class Gui(ttk.Frame):
    def __init__(self, dimension, master=None):
        super().__init__(master, width=800, height=800)
        self.dimension=dimension
        self.grid_propagate(0)
        self.grid(column=0, row=0)
        self.add_load_button()
        self.btn_arr = []
        self.add_grids()

    def add_grids(self):
        grids_frame = ttk.Frame(self, width=400, height=400)
        grids_frame.propagate(0)
        grids_frame.grid()
        grids_frame.columnconfigure(self.dimension+1)
        grids_frame.rowconfigure(self.dimension+1)
        for row, col in product(range(self.dimension), repeat=2):
            b = ButtonColor(grids_frame, width=1)
            b.grid(column=col, row=row)
            self.btn_arr.append(b)
