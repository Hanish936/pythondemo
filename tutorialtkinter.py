from tkinter import *
from PIL import Image,ImageTk
singh = Tk()
singh.geometry("500x500")
singh.minsize(50,50)
singh.maxsize(400,400)
singh.title("my page")
hanish =Label(text="this is my first GUI",bg="red",fg="white",padx=10,pady=10,font="comicsansms 20 bold")
#photo=PhotoImage(file="image name")
#image=Image.open("hanish.jpg")
#photo=ImageTk.PhotoImage(image)
#imagelabel=Label(image=photo)
#imagelabel.pack()
#attributes in gui

hanish.pack(anchor="sw",fill=Y)
singh.mainloop()