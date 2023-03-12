# from tkinter import *
import tkinter as tk
from tkinter import ttk
# tk._test()
from Base_clases.base import Add_bd

# def add_db():
#     new_win = tk.Toplevel(win)
#     new_win.geometry('250x300+500+300')
#     new_win.iconbitmap('./icons/base_data.ico')
#     exit_button = tk.Button(new_win,
#                             # image="gear.ico",
#                             new_win.title('Add new Database'),
#
#                             text="Cancel",
#                             activebackground='red',
#
#                             # compound=tk.LEFT,
#                             command=lambda: new_win.destroy()
#                             )
#     exit_button.pack()
#     new_win.mainloop()

win = tk.Tk()
h = 300
w = 250
win.title('Status DB')
win.iconbitmap('./icons/gear.ico')
win.geometry(f"{h}x{w}+400+300")

def add_db_win():
    window = Add_bd()

# add_db_button = tk.Button(win,
#                           text="Add database",
#                           activebackground='yellow',
#                           command=add_db,
#
#                           )

add_db_button = tk.Button(text="Add database", command=add_db_win)

exit_button = tk.Button(win,
                        # image="gear.ico",
                        text="Exit",
                        # compound=tk.LEFT,
                        activebackground='red',
                        command=lambda: win.destroy()
                        # command=lambda: win.quit()
                        )
add_db_button.pack()
exit_button.pack()
win.mainloop()
