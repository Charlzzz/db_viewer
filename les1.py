# from tkinter import *
import tkinter as tk
from tkinter import ttk
# from Base_clases.base import Add_bd
from tkinter import messagebox
from tkinter.messagebox import askyesno
import conDB
from tkinter.messagebox import showerror, showwarning, showinfo

# class ButtonFrame(ttk.Frame):
#
#     def __init__(self, container):
#         super().__init__(container)


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.h = 300
        self.w = 250
        self.title('Status DB')
        self.iconbitmap('./icons/gear.ico')
        self.geometry(f"{self.h}x{self.w}+400+300")
        self.resizable(False, True)
        # self.attributes('-toolwindow', True)
        self.getting_status()
        self.create_widgets()




    def update_label(self, dbname, status, counter):
        if status == True:
            self.db_label = tk.Label(self, text=dbname, background='green')
            self.db_label.grid(column=counter, row=1, sticky=tk.W, padx=5, pady=5)
        elif status == False:
            self.db_label = tk.Label(self, text=dbname, background='red')
            self.db_label.grid(column=counter, row=1, sticky=tk.W, padx=5, pady=5)

    def getting_status(self):

        with open('D:\\list_db_viewer.txt', 'r', encoding='utf-8') as read_list_dbfile:
            counter = 0
            res = read_list_dbfile.readlines()
            for i in res:
                counter += 1
                dbname, user, password, host, port = [a.strip() for a in i.split(" ")]
                status = conDB.conn(dbname, user, password, host, port)
                self.update_label(dbname, status, counter)
        counter = 0
        read_list_dbfile.close()
        self.after(15000, self.getting_status)


        # title_base =

    def add_db_win(self):
        window = Add_bd_frame()


    def create_widgets(self):
        add_db_button = tk.Button(text="Add database", command=self.add_db_win, activebackground='yellow')

        exit_button = tk.Button(self,
                                # image="gear.ico",
                                text="Exit",
                                # compound=tk.LEFT,
                                activebackground='red',
                                command=lambda: self.confirm()
                               )


        add_db_button.place(relx=.4, rely=.7, anchor='e')
        exit_button.place(relx=.8, rely=.7, anchor='w')

    def confirm(self):
        answer = askyesno(
            title='Confirmation',
            message='Are you sure to exit?',
        )
        if answer:
            self.destroy()



class Add_bd_frame(tk.Frame):


    def __init__(self):
        super().__init__()

        self.new_win = tk.Toplevel(self)
        self.new_win.geometry('350x300+500+300')
        self.new_win.iconbitmap('./icons/base_data.ico')
        self.new_win.title('Add new Database')
        # self.new_win.attributes('-topmost', 1)

        self.label_dbname = tk.Label(self.new_win, text="DBname:")
        self.label_dbname.pack(fill='x', expand=True)
        self.entry_dbname = tk.Entry(self.new_win)
        self.entry_dbname.pack(fill='x', expand=True)
        self.entry_dbname.focus()



        self.label_user = tk.Label(self.new_win, text="User:")
        self.label_user.pack(fill='x', expand=True)
        self.entry_user = tk.Entry(self.new_win)
        self.entry_user.pack(fill='x', expand=True)


        self.label_password = tk.Label(self.new_win, text="Password:")
        self.label_password.pack(fill='x', expand=True)
        self.entry_password = tk.Entry(self.new_win, show="*")
        self.entry_password.pack(fill='x', expand=True)


        self.label_host = tk.Label(self.new_win, text="Host:")
        self.label_host.pack(fill='x', expand=True)
        self.entry_host = tk.Entry(self.new_win)
        self.entry_host.pack(fill='x', expand=True)


        self.label_port = tk.Label(self.new_win, text="Port:")
        self.label_port.pack(fill='x', expand=True)
        self.entry_port = tk.Entry(self.new_win)
        self.entry_port.pack(fill='x', expand=True)


        self.exit_button = tk.Button(self.new_win,
                                  text="Cancel",
                                  activebackground='red',
                                  # compound=tk.LEFT,
                                  command=lambda: self.confirm()
                                  )
        self.exit_button.pack(side='left', ipady='10')

        # variable = messagebox.showinfo('Information', 'New DB has been successfully added.')
        self.submit_button = tk.Button(self.new_win,
                                  text="Submit",
                                  activebackground='yellow',
                                  # compound=tk.LEFT,
                                  command=lambda: self.send_properties()
                                  )
        # self.db_label = tk.Label(text='None')  # лейбл
        # self.db_label.pack()
        self.submit_button.pack(side='right', ipady='10')

        self.new_win.mainloop()

    def send_properties(self):
        port = self.entry_port.get()
        host = self.entry_host.get()
        password = self.entry_password.get()
        user = self.entry_user.get()
        dbname = self.entry_dbname.get()

        if conDB.conn(dbname, user, password, host, port) == True:
            conDB.add_db_to_text(dbname, user, password, host, port)
            messagebox.showinfo('Information', 'New DB has been successfully added.')
            self.new_win.destroy()

    def confirm(self):
        answer = askyesno(
            title='Confirmation',
            message='Cancel add database.'
        )
        if answer:
            self.new_win.destroy()

    def successful_add_db(self, used_window):
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()