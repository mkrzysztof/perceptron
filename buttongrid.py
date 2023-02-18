from itertools import product
from tkinter import ttk, filedialog
from math import sqrt

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


class ButtonGrid:
    def __init__(self, root, dimension):
        self.btn_array = []
        self.dimension = dimension
        self.root = root
        self.grids_frame = ttk.Frame(root, width=400, height=400)
        self.grids_frame.propagate(0)
        self.grids_frame.columnconfigure(self.dimension+1)
        self.grids_frame.rowconfigure(self.dimension+1)
        for row, col in product(range(self.dimension), repeat=2):
            b = ButtonColor(self.grids_frame, width=1)
            b.grid(column=col, row=row)
            self.btn_array.append(b)

    def grid(self, **kwargs):
        self.grids_frame.grid(**kwargs)

    def destroy(self):
        self.grids_frame.destroy()

    def save_grid(self, case_number, file):
        file.write(f"{case_number} ")
        file.write(f"{len(self.btn_array)} ")
        for btn in self.btn_array:
            file.write(f"{btn.cell} ")

    def save_pic(self, case_number):
        filename = filedialog.asksaveasfilename()
        with open(filename, "w") as f:
            self.save_grid(case_number, f)

    def load_grid(self, file):
        data = file.read().split()
        case_num = int(data[0])
        num_squares = int(data[1])
        dimension = int(sqrt(num_squares))
        # usunąć self.root.button_grid
        self.grids_frame.destroy()
        button_grid = ButtonGrid(self.root, dimension)
        for d, btn in zip(data[2:], button_grid.btn_array):
            if int(d) == 0:
                btn.cell = 0
                btn.configure(style="Green.TButton")
            else:
                btn.cell = 1
                btn.configure(style="Red.TButton")
        return case_num, button_grid

    def load_pic(self):
        filename = filedialog.askopenfilename()
        with open(filename, "r") as f:
            case_num, button_grid = self.load_grid(f)
        return case_num, button_grid
