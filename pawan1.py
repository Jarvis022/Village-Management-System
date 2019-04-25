from Tkinter import *
from p7 import rel
import webbrowser
import tkMessageBox
import sqlite3
from im import im3
from p3 import fx
from p4 import fx2
from splash import splas
con=sqlite3.Connection('mydb3')
cur=con.cursor()
cur.execute("create table if not exists vill2(ID varchar(20) PRIMARY KEY, name varchar(2), Password varchar(15) not null)")
def first():
    window = Tk()
    def dialog2():
        window.destroy()
        root=Tk()
        root.configure(background='white')
        Label(root,text="Village-Gahiya",font='Times 30 bold',bg='white').grid(row=0,column=1)
        Label(root,text="Post-Kamasin/Thana-Chillah/Block KONE/District-Mirzapur",font='Times 20 bold',bg='white').grid(row=1,column=1)
        Label(root,text="Projects In Vilages",font='Times 20 italic bold',bg='white').grid(row=2,column=0)
        Label(root,text="Village Leaders & Officers",font='Times 20 bold',bg='white').grid(row=2,column=5)
        def callback(event):
            webbrowser.open_new(r"http://mnregaweb2.nic.in/netnrega/IndexFrame.aspx?lflag=local&District_Code=3162&district_name=MIRZAPUR&state_name=%E0%A4%89%E0%A4%A4%E0%A5%8D%E0%A4%A4%E0%A4%B0%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%A6%E0%A5%87%E0%A4%B6&state_Code=31&block_name=KON&block_code=3162002&fin_year=2017-2018&check=1&Panchayat_name=GAHIYA&Panchayat_Code=3162002034")
        link = Label(root, text="MGNREGA",font='Times 15 bold', fg="blue", cursor="hand2",bg='white')
        link.grid(row=3,column=0)
        link.bind("<Button-1>", callback)
        def callback(event):
            webbrowser.open_new(r"http://pmayg.nic.in/netiay/photogallery.aspx")
        link = Label(root, text="PMGAY",font='Times 15 bold', fg="blue", cursor="hand2",bg='white')
        link.grid(row=4,column=0)
        link.bind("<Button-1>", callback)
        def callback(event):
            webbrowser.open_new(r"https://resident.uidai.gov.in/check-aadhaar-status")
        link = Label(root, text="Adhar",font='Times 15 bold', fg="blue", cursor="hand2",bg='white')
        link.grid(row=5,column=0)
        link.bind("<Button-1>", callback)
        def callback(event):
            webbrowser.open_new(r"http://www.nvsp.in/forms/forms/trackstatus")
        link = Label(root, text="VoterId",font='Times 15 bold', fg="blue", cursor="hand2",bg='white')
        link.grid(row=6,column=0)
        link.bind("<Button-1>", callback)
        def callback(event):
            webbrowser.open_new(r"https://tin.tin.nsdl.com/pantan/StatusTrack.html")
        link = Label(root, text="Pan card",font='Times 15 bold', fg="blue", cursor="hand2",bg='white')
        link.grid(row=7,column=0)
        link.bind("<Button-1>", callback)
        def sar():
            root3=Toplevel()
            a=PhotoImage(file="new.gif")
            Label(root3,image=a).grid(row=5,column=2)
            Label(root3,text="Name: Mr. Subhash Chandra Mishra",font='Times 20 bold').grid(row=1,column=2)
            Label(root3,text="Contact: 7839270200",font='Times 20 bold').grid(row=2,column=2)
            Label(root3,text="Correspondence Adress: Apartment no-B1/204 Tridev Apartment Varanasi",font='Times 20 bold').grid(row=3,column=2)
            Label(root3,text="EmailId: subhashchandra123@gmail.com",font='Times 20 bold').grid(row=4,column=2)
            root3.mainloop()
        Button(root,text='Sarpanch',font='Times 15 bold',bg='grey',command=sar,bd=10).grid(row=3,column=5)
        def sar1():
            root4=Toplevel()
            a=PhotoImage(file="srb.gif")
            Label(root4,image=a).grid(row=5,column=2)
            Label(root4,text="Name: Mr. Harishankar Pandey",font='Times 20 bold').grid(row=1,column=2)
            Label(root4,text="Contact: 9893443003",font='Times 20 bold').grid(row=2,column=2)
            Label(root4,text="Correspondence Adress:H-No-133 Chillah Block-Kone District-Mirzapur",font='Times 20 bold').grid(row=3,column=2)
            Label(root4,text="EmailId: Harishankar123@gmail.com",font='Times 20 bold').grid(row=4,column=2)
            root4.mainloop()

        Button(root,text='Secretary',font='Times 15 bold',bg='grey',command=sar1,bd=10).grid(row=4,column=5)
        def sar2():
            root4=Toplevel()
            a=PhotoImage(file="pranjal.gif")
            Label(root4,image=a).grid(row=5,column=2)
            Label(root4,text="Name: Mr. Neeraj Dubey",font='Times 20 bold').grid(row=1,column=2)
            Label(root4,text="Contact: 9415257607",font='Times 20 bold').grid(row=2,column=2)
            Label(root4,text="Correspondence Adress: Teachers Colony Wesliganj Mirzapur",font='Times 20 bold').grid(row=3,column=2)
            Label(root4,text="EmailId: dubeyNeeraj123@gmail.com",font='Times 20 bold').grid(row=4,column=2)
            root4.mainloop()
        Button(root,text='B.D.O.',font='Times 15 bold',bg='grey',command=sar2,bd=10).grid(row=5,column=5)
        def sar3():
            root4=Toplevel()
            a=PhotoImage(file="ADO.gif")
            Label(root4,image=a).grid(row=5,column=2)
            Label(root4,text="Name: Mr. Vinod Gaud",font='Times 20 bold').grid(row=1,column=2)
            Label(root4,text="Contact: 7685989625",font='Times 20 bold').grid(row=2,column=2)
            Label(root4,text="Correspondence Adress: H-n0.133/4 Railway Colony Mirzapur",font='Times 20 bold').grid(row=3,column=2)
            Label(root4,text="EmailId: vinodGaud23@gmail.com",font='Times 20 bold').grid(row=4,column=2)
            root4.mainloop()
        Button(root,text='A.D.O.',font='Times 15 bold',bg='grey',command=sar3,bd=10).grid(row=6,column=5)
        def sar4():
            root4=Toplevel()
            a=PhotoImage(file="BDC.gif")
            Label(root4,image=a).grid(row=5,column=2)
            Label(root4,text="Name: Mrs. Sheela Devi",font='Times 20 bold').grid(row=1,column=2)
            Label(root4,text="Contact: 7475714258",font='Times 20 bold').grid(row=2,column=2)
            Label(root4,text="Correspondence Adress: Ravani Parivar Gahiya Chillah Mirzapur",font='Times 20 bold').grid(row=3,column=2)
            Label(root4,text="EmailId: Ravani.yadav3@gmail.com",font='Times 20 bold').grid(row=4,column=2)
            root4.mainloop()
        Button(root,text='B.D.C.',font='Times 15 bold',bg='grey',command=sar4,bd=10).grid(row=7,column=5)
        Button(root,text='MNREGA Attendance',font='Times 15 bold',bg='white',fg='blue',command=fx,bd=10).grid(row=3,column=1)
        Button(root,text='Teachers Attendance',font='Times 15 bold',bg='white',fg='blue',command=fx2,bd=10).grid(row=4,column=1)
        Button(root,text='MAPS',font='Times 15 bold',bg='white',fg='blue',command=im3,bd=10).grid(row=5,column=1)
        Button(root,text='Members',font='Times 15 bold',bg='white',fg='blue',command=rel,bd=10).grid(row=6,column=1)
        root.mainloop()
    window.title('Countries Generation')
    frame = Frame(window)
    Label1 = Label(window,text = 'Username:').grid(column=0,row=0)
    entry1 = Entry(window,bd =5)
    entry1.grid(column=1,row=0)
    Label2 = Label(window,text = 'Password: ').grid(column=0,row=1)
    entry2 = Entry(window,show='*', bd=5)
    entry2.grid(column=1,row=1)
    def dialog1():
        cur.execute('select Password from vill2 where ID = ?',(entry1.get(),))
        b = cur.fetchall()
        n=entry2.get()
        if n == b[0][0]:
            dialog2()
        else:
            print "NO LOGIN"
    def fun():
        root2=Tk()
        Label(root2,text='UserId:').grid(row=1,column=1)
        e4=Entry(root2,bd=10)
        e4.grid(row=1,column=2)
        Label(root2,text='Name:').grid(column=1,row=2)
        e1=Entry(root2,bd=10)
        e1.grid(row=2,column=2)
        
        Label(root2,text='Password:').grid(column=1,row=3)
        e2=Entry(root2,bd=10)
        e2.grid(row=3,column=2)
        Label(root2,text='Confirm Password:').grid(column=1,row=4)
        e3=Entry(root2,bd=10)
        e3.grid(row=4,column=2)
        def getc():
              if(e3.get()==e2.get()):
                        a=[e4.get(),e1.get(),e2.get()]
                        cur.execute("insert into vill2 values(?,?,?)",a)
                        con.commit()
                        root2.destroy()
                        first()
        Button(root2,text='Sign Up',command=getc).grid(column=2,row=5)
        root2.mainloop()
    btn = Button(window, text ='Login', command = dialog1).grid(column=0,row=2)
    btn1=Button(window,text='New Login',command=fun).grid(column=1,row=2)
    window.mainloop()
splas()
first()
