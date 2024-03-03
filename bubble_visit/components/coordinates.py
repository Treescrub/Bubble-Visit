from tkinter import ttk


class SectorCoordinates(ttk.Frame):
    def __init__(self, parent):
        super().__init__()

        coordinate_frame = ttk.LabelFrame(parent, text="Coordinates", padding=10)
        coordinate_frame.pack()

        ttk.Label(coordinate_frame, text="X", padding=5).grid(row=0, column=0)
        ttk.Entry(coordinate_frame, width=5).grid(row=0, column=1)
        ttk.Label(coordinate_frame, text="Y", padding=5).grid(row=1, column=0)
        ttk.Entry(coordinate_frame, width=5).grid(row=1, column=1)
        ttk.Label(coordinate_frame, text="Z", padding=5).grid(row=2, column=0)
        ttk.Entry(coordinate_frame, width=5).grid(row=2, column=1)
