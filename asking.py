"""asking training perceptron"""
import math
import pickle
from tkinter import ttk
from buttongrid import ButtonGrid
from perceptron import Perceptron


WIDTH = 800
HEIGHT = 800

class Asking:
    def __init__(self, perceptron):
        self.root_window = ttk.Frame(None, width=WIDTH, height=HEIGHT)
        self.button_grid = ButtonGrid(
            self.root_window, int(math.sqrt(perceptron.r))
        )
        self.root_window.grid_propagate(0)
        self.root_window.grid()
        self.button_grid.grid()
        self.button = ttk.Button(
            self.root_window, text='SPRAWDŹ'
        )
        self.button.grid()
        self.recognized = ttk.Entry()
        self.recognized.grid()
        self.root_window.mainloop()

if __name__ == "__main__":
    perceptron = Perceptron(8*8, 4)
    ask = Asking(perceptron)
