"""asking training perceptron"""
from array import array
import math
import pickle
from tkinter import ttk
from buttongrid import ButtonGrid
from perceptron import Perceptron


WIDTH = 800
HEIGHT = 800

class Asking:
    def __init__(self, perceptron):
        self.perceptron = perceptron
        self.root_window = ttk.Frame(None, width=WIDTH, height=HEIGHT)
        self.button_grid = ButtonGrid(
            self.root_window, int(math.sqrt(perceptron.r))
        )
        self.root_window.grid_propagate(0)
        self.root_window.grid()
        self.button_grid.grid()
        self.button = ttk.Button(
            self.root_window, text='SPRAWDŹ', command=self.recognize
        )
        self.button.grid()
        self.recognized = ttk.Entry()
        self.recognized.grid()
        self.root_window.mainloop()

    def recognize(self):
        rec_vector = evaluate(self.perceptron, self.button_grid)
        list_recogn = [i for i, elem in enumerate(rec_vector) if elem == 1]
        self.recognized.delete(
            0,
            len(self.recognized.get())
        )
        for num in list_recogn:
            self.recognized.insert(0, f'{num} ')

def evaluate(perceptron, button_grid):
    x = array("d", [int(btn.cell) for btn in button_grid.btn_array])
    return perceptron.evaluate(x)

if __name__ == "__main__":
    with open("serializacja1", "rb") as f:
        perceptron1 = pickle.load(f)
    perceptron = Perceptron(8*8, 4)
    ask = Asking(perceptron1)
