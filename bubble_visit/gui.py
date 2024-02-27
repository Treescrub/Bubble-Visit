from tkinter import *
from tkinter import ttk


VERSION = "0.1.0"


def run():
    window = Tk()
    window.title("Bubble Visit")
    window.option_add("*tearOff", FALSE)

    frame = ttk.Frame(window, padding=10)
    frame.pack()

    system_count_frame = ttk.Frame(frame, padding=10)
    system_count_frame.pack()

    sector_sys_label = ttk.Label(system_count_frame, text="Visited systems in sector: 0")
    sector_sys_label.pack()

    bounds_sys_label = Label(system_count_frame, text="Visited systems in bounds: 0")
    bounds_sys_label.pack()

    button = ttk.Button(frame, text="Complete sector")
    button.pack()

    menubar = Menu(window)
    window["menu"] = menubar

    menu_file = Menu(menubar)
    menu_file.add_command(label="Test")

    menubar.add_cascade(menu=menu_file, label="File")

    window.mainloop()
