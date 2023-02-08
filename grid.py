# program do tworzenie pixelowych obrazków w 2 kolorach
# a następnie ich zapisywania w formie pojedyńczego wektora
from itertools import product
from math import sqrt
from tkinter import ttk
from tkinter import filedialog


s = ttk.Style()
s.configure("Red.TButton", background="red")
s.configure("Green.TButton", background="green")


class ButtonColor(ttk.Button):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.configure(command=self.switch)
        self.cell = 0
        self.configure(style="Green.TButton")

    def switch(self):
        if self.cell == 0:
            self.configure(style="Red.TButton")
            self.cell = 1
        else:
            self.configure(style="Green.TButton")
            self.cell = 0

            
class Net(ttk.Frame):
    def __init__(self, dimension, master=None):
        super().__init__(master, width=800, height=800)
        self.dimension=dimension
        self.grid_propagate(0)
        self.grid(column=0, row=0)
        self.btn_arr = []
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
        grids_frame = ttk.Frame(self, width=400, height=400)
        grids_frame.propagate(0)
        grids_frame.grid()
        grids_frame.columnconfigure(self.dimension+1)
        grids_frame.rowconfigure(self.dimension+1)
        for row, col in product(range(self.dimension), repeat=2):
            b = ButtonColor(grids_frame, width=1)
            b.grid(column=col, row=row)
            self.btn_arr.append(b)
            
def save_grid(net, file):
    file.write(f"{net.entry_case.get()} ")
    file.write(f"{len(net.btn_arr)} ")
    for btn in net.btn_arr:
        file.write(f"{btn.cell} ")

def save_pic(net):
    filename = filedialog.asksaveasfilename()
    with open(filename, "w") as f:
        save_grid(net, f)

def load_grid(file):
    data = file.read().split()
    case_num = int(data[0])
    num_squares = int(data[1])
    dimension = int(sqrt(num_squares))
    net = Net(dimension)
    net.entry_case.insert(0, str(case_num))
    for d, btn in zip(data[2:], net.btn_arr):
        if int(d) == 0:
            btn.cell = 0
            btn.configure(style="Green.TButton")
        else:
            btn.cell = 1
            btn.configure(style="Red.TButton")
            
def load_pic():
    filename = filedialog.askopenfilename()
    with open(filename, "r") as f:
        load_grid(f)

    
if __name__ == '__main__':
    net = Net(5)
    net.mainloop()
    
