from tkinter import *
def getvalue():
    print(uservalue.get())
    print(passvalue.get())
root=Tk()
root.geometry("500x500")
username=Label(root,text="Username")
password=Label(root,text="password")
username.grid()
password.grid()
uservalue=StringVar()
passvalue=StringVar()
userentry=Entry(root,textvariable=uservalue)
passentry=Entry(root,textvariable=passvalue)
userentry.grid(row=0,column=1)
passentry.grid(row=1,column=1)
Button(root,bg="grey",borderwidth=6,text="login",command=getvalue).grid()



root.mainloop()