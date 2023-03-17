import tkinter as tk

class Example:
    def __init__(self):
        self.root = tk.Tk()
        self.fade_in_var = tk.BooleanVar()
        self.fade_in_var.trace('w', self.update_fade_in)
        self.fade_in_ck = tk.Checkbutton(self.root, text="Fade-in", variable=self.fade_in_var)
        self.fade_in_ck.pack()
        self.fade_in_sc = tk.Scale(self.root, from_=0, to=10, orient=tk.HORIZONTAL, resolution=1, state=tk.DISABLED)
        self.fade_in_sc.pack()
        self.root.mainloop()

    def update_fade_in(self, *args):
        if self.fade_in_var.get():
            self.fade_in_sc.config(state='normal')
        else:
            self.fade_in_sc.config(state='disabled')

Example()