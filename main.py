#! python3

from tkinter import *
from tkinter import ttk
from PLdb import *

app = Tk()
app.title('PWDM')
app.resizable(False, False)

label_user = ttk.Label(app, text='Username:')
label_user.grid(row=0, column=0)

entry_user = ttk.Entry(app, width=30)
entry_user.grid(row=1, column=0)


def new():
    label_pass = ttk.Label(app, text='Password:')
    entry_pass = ttk.Entry(app, width=30)

    label_pass.grid(row=2, column=0)
    entry_pass.grid(row=3, column=0)
    
    button_new.state(['disabled'])

    def add():
        nac = entry_user.get()
        npwd = entry_pass.get()
        msg = db_w(nac, npwd)
        print(msg)

    button_add = ttk.Button(text='Add Account', command=add)
    button_add.grid(row=4, column=0)

def show():
    label_frame = ttk.LabelFrame(app, text='Your Password:')

    pwd = entry_user.get()

    label = ttk.Label(label_frame, text=db_r(pwd))
    label.config(font=('courier', 25, 'italic'), foreground = 'red', background = 'yellow')

    label_frame.grid()
    label.grid()

button_new = ttk.Button(app, text='New account', command=new)
button_new.grid(row=4, column=0)

button_show = ttk.Button(app, text='Show Password', command=show)
button_show.grid()

app.mainloop()
