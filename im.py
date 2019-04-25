from Tkinter import *
def im3():
    top=Toplevel()
    a=PhotoImage(file='map.gif')
    lb=Label(top,image=a)
    lb.pack()
    top.mainloop()
