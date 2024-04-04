import tkinter
from tkinter import ttk
from tkinter import *


class Settings(tkinter.Toplevel):
    sector_size = None
    bounds_size = None

    def __init__(self, parent):
        super().__init__(parent)

        self.sector_size = DoubleVar()
        self.bounds_size = DoubleVar()

        frame = ttk.Frame(self)
        frame.pack(fill=BOTH, expand=TRUE)

        canvas = Canvas(frame)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

        scrollbar = ttk.Scrollbar(frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        canvas.configure(yscrollcommand=scrollbar.set)

        sector_size_label = ttk.Label(canvas, text="Sector size")
        sector_size_label.pack(anchor=CENTER)
        sector_size_entry = ttk.Entry(canvas, textvariable=self.sector_size)
        sector_size_entry.pack(anchor=CENTER)

        bounds_size_label = ttk.Label(canvas, text="Bounds size")
        bounds_size_label.pack(anchor=CENTER)
        bounds_size_entry = ttk.Entry(canvas, textvariable=self.bounds_size)
        bounds_size_entry.pack(anchor=CENTER)
