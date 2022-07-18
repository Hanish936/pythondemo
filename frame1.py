from tkinter import *
def name():
    print("hello to all")
root=Tk()
root.geometry("500x500")
f=Frame(root,bg="grey",borderwidth=6,relief=SUNKEN)
f.pack(side=LEFT)
l=Label(f,text="hello frames")
l.pack(pady=30)
b1=Button(root,bg="grey",borderwidth=6,relief=SUNKEN,text="print now", command=name)
b1.pack()
root.mainloop()