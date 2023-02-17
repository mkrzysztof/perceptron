from tkinter import ttk


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
