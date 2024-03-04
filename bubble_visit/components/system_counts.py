from tkinter import ttk


class SystemCounts(ttk.LabelFrame):
    def __init__(self, parent):
        super().__init__(parent, text="Systems", padding=10)

        sector_sys_label = ttk.Label(self, text="Visited systems in sector: 0")
        sector_sys_label.grid(row=0, column=0)

        bounds_sys_label = ttk.Label(self, text="Visited systems in bounds: 0")
        bounds_sys_label.grid(row=1, column=0)
