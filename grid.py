# program do tworzenie pixelowych obrazków w 2 kolorach
# a następnie ich zapisywania w formie pojedyńczego wektora

from math import sqrt
from tkinter import ttk
from tkinter import filedialog
from buttongrid import ButtonColor, ButtonGrid



            
class Net(ttk.Frame):
    def __init__(self, dimension, master=None):
        super().__init__(master, width=800, height=800)
        self.dimension=dimension
        self.grid_propagate(0)
        self.grid(column=0, row=0)
        self.add_save_load_button()
        self.add_entry()
        self.add_grids()

    def add_entry(self):
        self.entry_case = ttk.Entry(self, width=6)
        self.entry_case.grid()
        
        
    def add_save_load_button(self):
        load_save_frame = ttk.Frame(self, width=600, height=100)
        load_save_frame.grid_propagate(0)
        load_save_frame.grid()
        self.save_btn = ttk.Button(
            load_save_frame, text="Save",
            command=lambda: save_pic(self))
        self.load_btn = ttk.Button(
            load_save_frame, text="Load",
            command=load_pic
        )
        self.save_btn.grid(column=1, row=1)
        self.load_btn.grid(column=2, row=1)

    def add_grids(self):
        self.button_grid = ButtonGrid(self, self.dimension)

def save_pic(net):
    net.button_grid.save_pic(int(net.entry_case.get()))

            
def load_pic():
    case_num = net.button_grid.load_pic()
    text = net.entry_case.get()
    if text:
        net.entry_case.delete(0, len(text))
    net.entry_case.insert(0, str(case_num))


if __name__ == '__main__':
    net = Net(8)
    net.mainloop()
    
