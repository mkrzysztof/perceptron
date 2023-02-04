# program do tworzenie pixelowych obrazków w 2 kolorach
# a następnie ich zapisywania w formie pojedyńczego wektora
from tkinter import ttk
from tkinter import filedialog

class ButtonColor(ttk.Button):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.configure(command=self.switch)
        self.cell = 0
        s = ttk.Style()
        s.configure("Red.TButton", background="red")
        s.configure("Green.TButton", background="green")
        self.configure(style="Green.TButton")

    def switch(self):
        if self.cell == 0:
            self.configure(style="Red.TButton")
            self.cell = 1
        else:
            self.configure(style="Green.TButton")
            self.cell = 0

            
class Net(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, width=800, height=800)
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
            command=lambda: save_pic(self.btn_arr))
        self.load_btn = ttk.Button(load_save_frame, text="Load")
        self.save_btn.grid(column=1, row=1)
        self.load_btn.grid(column=2, row=1)

    def add_grids(self):
        NUM_OF_BUTT = 20
        grids_frame = ttk.Frame(self, width=400, height=400)
        grids_frame.propagate(0)
        grids_frame.grid()
        grids_frame.columnconfigure(NUM_OF_BUTT+1)
        grids_frame.rowconfigure(NUM_OF_BUTT+1)
        for col in range(NUM_OF_BUTT):
            for row in range(NUM_OF_BUTT):
                b = ButtonColor(grids_frame, width=1)
                b.grid(column=col, row=row)
                self.btn_arr.append(b)

def save_grid(btn_arr, file):
    file.write(f"{self.entry_case.get()} ")
    file.write(f"{len(btn_arr)} ")
    for btn in btn_arr:
        file.write(f"{btn.cell} ")

def save_pic(btn_arr):
    filename = filedialog.asksaveasfilename()
    with open(filename, "w") as f:
        save_grid(btn_arr, f)

if __name__ == '__main__':
    net = Net()
    net.mainloop()
    
