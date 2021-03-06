from Tkinter import *
import sqlite3
con=sqlite3.Connection('mydb5')
cur=con.cursor()
cur.execute("create table if not exists vill4(ID integer PRIMARY KEY autoincrement, name varchar(2), AID int not null,FName varchar(20),MName varchar(20),Adress varchar(50),Salary int)")
def rel():
    root=Tk()
    def view():
        root1=Toplevel()
        Label(root1,text="ID",font="times 15 bold").grid(row=0,column=1,columnspan=1,padx=20)
        Label(root1,text="Name",font="times 15 bold").grid(row=0,column=2,columnspan=1,padx=20)
        Label(root1,text="Aadhar No.",font="times 15 bold").grid(row=0,column=3,columnspan=1,padx=20)
        Label(root1,text="Father's Name",font="times 15 bold").grid(row=0,column=4,columnspan=1,padx=20)
        Label(root1,text="Mother's Name",font="times 15 bold").grid(row=0,column=5,columnspan=1,padx=20)
        Label(root1,text="Adress",font="times 15 bold").grid(row=0,column=6,columnspan=1,padx=20)
        Label(root1,text="Salary",font="times 15 bold").grid(row=0,column=7,columnspan=1,padx=20)
        cur.execute("select max(ID) from vill4")
        z=cur.fetchall()
        for i in range(1,z[0][0]):
            k=[i]
            cur.execute("select * from vill4 where ID=(?)",k)
            b=cur.fetchall()
            Label(root1,text=b[0][0],font="times 15 bold").grid(row=i,column=1,columnspan=1,padx=20)
            Label(root1,text=b[0][1],font="times 15 bold").grid(row=i,column=2,columnspan=1,padx=20)
            Label(root1,text=b[0][2],font="times 15 bold").grid(row=i,column=3,columnspan=1,padx=20)
            Label(root1,text=b[0][3],font="times 15 bold").grid(row=i,column=4,columnspan=1,padx=20)
            Label(root1,text=b[0][4],font="times 15 bold").grid(row=i,column=5,columnspan=1,padx=20)
            Label(root1,text=b[0][5],font="times 15 bold").grid(row=i,column=6,columnspan=1,padx=20)
            Label(root1,text=b[0][6],font="times 15 bold").grid(row=i,column=7,columnspan=1,padx=20)
        root1.mainloop()
    def add():
        root2=Toplevel()
        Label(root2,text="Name:").grid(row=1,column=1)
        e1=Entry(root2)
        e1.grid(row=1,column=2)
        Label(root2,text="AID:").grid(row=2,column=1)
        e2=Entry(root2)
        e2.grid(row=2,column=2)
        Label(root2,text="Father's Name:").grid(row=3,column=1)
        e3=Entry(root2)
        e3.grid(row=3,column=2)
        Label(root2,text="Mother's Name:").grid(row=4,column=1)
        e4=Entry(root2)
        e4.grid(row=4,column=2)
        Label(root2,text="Adress:").grid(row=5,column=1)
        e5=Entry(root2)
        e5.grid(row=5,column=2)
        Label(root2,text="Salary:").grid(row=6,column=1)
        e6=Entry(root2)
        e6.grid(row=6,column=2)
        def update():
            a=[str(e1.get()),int(e2.get()),str(e3.get()),str(e4.get()),str(e5.get()),int(e6.get())]
            cur.executemany("insert into vill4 (name,AID,FName,MName,Adress,Salary) values (?,?,?,?,?,?)",(a,))
            con.commit()
        Button(root2,text="ADD",command=update).grid(row=7,column=2)
        root2.mainloop()
    Button(root,text="SEE ALL MEMBERS",command=view).pack()
    Button(root,text="ADD MEMBER",command=add).pack()
    root.mainloop()
