from tkinter import ttk
from tkinter import IntVar


class SectorCoordinates(ttk.LabelFrame):
    x = None
    y = None
    z = None

    def __init__(self, parent):
        super().__init__(parent, text="Coordinates", padding=10)

        self.x = IntVar()
        self.y = IntVar()
        self.z = IntVar()

        ttk.Label(self, text="X", padding=5).grid(row=0, column=0)
        ttk.Entry(self, width=5, textvariable=self.x).grid(row=0, column=1)
        ttk.Label(self, text="Y", padding=5).grid(row=1, column=0)
        ttk.Entry(self, width=5, textvariable=self.y).grid(row=1, column=1)
        ttk.Label(self, text="Z", padding=5).grid(row=2, column=0)
        ttk.Entry(self, width=5, textvariable=self.z).grid(row=2, column=1)
