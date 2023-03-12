from tkinter import *
from tkinter import ttk


class Add_bd():
    def __init__(self):
        super().__init__()
        self.new_win = Toplevel()
        self.new_win.geometry('350x300+500+300')
        self.new_win.iconbitmap('./icons/base_data.ico')
        self.new_win.title('Add new Database')
        self.exit_button = Button(self.new_win,
                                # image="gear.ico",
                                # self.new_win.title('Add new Database'),
                                text="Cancel",
                                activebackground='red',
                                # compound=tk.LEFT,
                                command=lambda: self.dismiss(self.new_win)
                                )
        self.exit_button.pack()
        self.new_win.mainloop()

    def dismiss(window):
        window.grab_release()
        window.destroy()




