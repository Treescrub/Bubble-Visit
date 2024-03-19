import tkinter as tk
from tkinter import ttk
from tkinter import IntVar
import re


class SectorCoordinates(ttk.LabelFrame):
    x = None
    y = None
    z = None

    def __init__(self, parent):
        super().__init__(parent, text="Coordinates", padding=10)

        self.x = IntVar()
        self.y = IntVar()
        self.z = IntVar()

        check_int_wrapper = (self.register(check_int), "%P")

        ttk.Label(self, text="X", padding=5).grid(row=0, column=0)
        x_entry = ttk.Entry(self, width=5, textvariable=self.x,
                            validate='all', validatecommand=check_int_wrapper
                            )
        x_entry.grid(row=0, column=1)
        x_entry.bind("<FocusOut>", lose_focus)

        ttk.Label(self, text="Y", padding=5).grid(row=1, column=0)
        y_entry = ttk.Entry(self, width=5, textvariable=self.y,
                            validate='all', validatecommand=check_int_wrapper
                            )
        y_entry.grid(row=1, column=1)
        y_entry.bind("<FocusOut>", lose_focus)

        ttk.Label(self, text="Z", padding=5).grid(row=2, column=0)
        z_entry = ttk.Entry(self, width=5, textvariable=self.z,
                            validate='all', validatecommand=check_int_wrapper
                            )
        z_entry.grid(row=2, column=1)
        z_entry.bind("<FocusOut>", lose_focus)


def lose_focus(event):
    entry = event.widget
    value = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, str(parse_int(value)))


def parse_int(int_str: str) -> int:
    if len(int_str) == 0:
        return 0

    return int(int_str)


def check_int(new_value):
    return re.match("^[0-9]*$", new_value) is not None
