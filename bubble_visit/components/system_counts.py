from tkinter import ttk


class SystemCounts(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        system_count_frame = ttk.LabelFrame(parent, text="Systems", padding=10)
        system_count_frame.pack()

        sector_sys_label = ttk.Label(system_count_frame, text="Visited systems in sector: 0")
        sector_sys_label.pack()

        bounds_sys_label = ttk.Label(system_count_frame, text="Visited systems in bounds: 0")
        bounds_sys_label.pack()
