from tkinter import *
from tkinter import messagebox

from mysql import connector


def database():
    conn = connector.connect(user='root', password='root', host='127.0.0.1', port='3306', database='demo1')
    mycursor = conn.cursor()
    mycursor.execute("insert int form values (%s,%d,%s,%d)", (c.get(), j.get(), e.get(), h.get()))
    conn.commit()


root = Tk()
root.geometry('500x500')
root.title("Registration Form")

a = Label(root, text="Registration form", width=20, font=("bold", 20))
a.place(x=60, y=30)

b = Label(root, text="FullName", width=20, font=("bold", 10))
b.place(x=80, y=130)

c = Entry(root)
c.place(x=240, y=130)

i = Label(root, text="Roll Number", width=20, font=("bold", 10))
i.place(x=80, y=180)

j = Entry(root)
j.place(x=240, y=180)

d = Label(root, text="Email", width=20, font=("bold", 10))
d.place(x=80, y=230)

e = Entry(root)
e.place(x=240, y=230)

g = Label(root, text="Age:", width=20, font=("bold", 10))
g.place(x=80, y=330)

h = Entry(root)
h.place(x=240, y=330)

Button(root, text='Submit', width=20, bg='brown', fg='white', command=database).place(x=180, y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  successfully created...")
