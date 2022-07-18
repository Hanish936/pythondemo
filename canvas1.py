from tkinter import *
def myfun():
    print("this is nothingand ")
root=Tk()
#canvas_width=400
#canvas_height=400
#root.geometry(f"{canvas_width}x{canvas_height}")
#can=Canvas(root,width=canvas_width,height=canvas_width)
#can.grid()
#can.create_line(0,0,50,50)
#can.create_rectangle(30,30,50,50)
#can.create_oval(60,80,70,80)

#widget=Button(root,text="event")
#widget.grid()
#widget.bind('<Button-1>',harry)
#widget.bind('<Double-1>',quit)
filemenu=Menu(root)
m1=Menu(filemenu,tearoff=0)
m1.add_command(label="new project",command=myfun)
m1.add_command(label="save as",command=myfun)
m1.add_command(label="save",command=myfun)
m1.add_command(label="open as",command=myfun)
root.config(menu=filemenu)
filemenu.add_cascade(label="file",menu=m1)
root.mainloop()