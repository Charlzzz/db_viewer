from tkinter import *
from tkinter import ttk
from tkinter.messagebox import askokcancel, showinfo, askyesno
import tkinter as tk

# from les1 import dbname, user, password, host, port


class Add_bd():

    user = StringVar()
    password = StringVar()
    host = StringVar()
    port = StringVar()
    def __init__(self):
        super().__init__()
        self.new_win = Toplevel()
        self.new_win.geometry('350x300+500+300')
        self.new_win.iconbitmap('./icons/base_data.ico')
        self.new_win.title('Add new Database')
        # self.new_win.attributes('-topmost', 1)

        self.label_dbname = Label(text="DBname:")
        self.label_dbname.pack(fill='x', expand=True)
        self.entry_dbname = Entry(textvariable=self.dbname)
        self.entry_dbname.pack(fill='x', expand=True)
        self.entry_dbname.focus()
        self.dbname = tk.StringVar()

        self.label_user = Label(text="User:")
        self.label_user.pack(fill='x', expand=True)
        self.entry_user = Entry(textvariable=user)
        self.entry_user.pack(fill='x', expand=True)

        self.label_password = Label(text="Password:")
        self.label_password.pack(fill='x', expand=True)
        self.entry_password = Entry(textvariable=password)
        self.entry_password.pack(fill='x', expand=True)

        self.label_host = Label(text="Host:")
        self.label_host.pack(fill='x', expand=True)
        self.entry_host = Entry(textvariable=host)
        self.entry_host.pack(fill='x', expand=True)

        self.label_port = Label(text="Port:")
        self.label_port.pack(fill='x', expand=True)
        self.entry_port = Entry(textvariable=port)
        self.entry_port.pack(fill='x', expand=True)

        self.exit_button = Button(self.new_win,
                                  text="Cancel",
                                  activebackground='red',
                                  # compound=tk.LEFT,
                                  command=lambda: self.confirm()
                                  )
        self.exit_button.place(relx=.8, rely=.7, anchor='e')

        self.new_win.mainloop()

    def confirm(self):
        answer = askyesno(
            title='Confirmation',
            message='Cancel add database.',
        )
        if answer:
            self.new_win.destroy()
