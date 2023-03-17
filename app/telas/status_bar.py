from tkinter import *
from tkinter import ttk

class Status_Bar():
    def __init__(self, root) -> None:
        self.botton_frame = Frame(root, relief=SUNKEN, bd=1)
        self.botton_frame.pack(side=BOTTOM, padx=5, pady=5, fill=X)
        
        status_label = Label(self.botton_frame, text='Status: pronto', relief=SUNKEN, anchor=W)
        status_label.pack(side=LEFT, fill=X, expand=YES)
        
        progress_bar = ttk.Progressbar(self.botton_frame, orient=HORIZONTAL, length=500, mode='determinate')
        progress_bar.pack(side=RIGHT, padx=2, pady=2)