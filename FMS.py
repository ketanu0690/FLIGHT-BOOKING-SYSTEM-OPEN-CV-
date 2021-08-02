#flight booking system with facial recogination

from tkcalendar import*
from tkinter import *
import mysql.connector as connector
import cv2
from PIL import ImageTk,Image
from tkinter import ttk,messagebox
from time import strftime

class login:
    def __init__(self,root):
        

        self.root=root
        self.root.title('Flight booking system')
        self.root.geometry("1100x600+100+50")
        self.root.resizable(False,False)
        
        
        self.ico =Image.open(r"D:\phython\FMS\FLIGHT-BOOKING-SYSTEM-OPEN-CV-\main2.jpg")

        self.ico = self.ico.resize((1100, 600),Image.ANTIALIAS)
        self.photo =ImageTk.PhotoImage(self.ico)
        self.root.iconphoto(False,self.photo)
        self.bg_image=Label(self.root,image=self.photo).place(x=0,y=0,relwidth=1,relheight=1)

        menubar= Menu(self.root,background='black',fg="white")
        filemenu= Menu(menubar,tearoff=1)
        menubar.add_command(label="AIRLINE BOOKING SYSTEM")
        
        menubar.add_command(label="LOGIN",command=self.loginfrm)
        
        menubar.add_command(label="HELP")  

        filemenu.add_separator() 
        menubar.add_command(label="EXIT",command=self.root.quit)

        self.root.config(menu=menubar)

        intro=Label(self.root,text='''WELCOME TO FLIGHT BOOKING SYSTEM
        
        Book your next flight !! ''',font=("Nirmala UI",25),bg="black",fg="white",bd=0).place(x=20,y=20)
        

    def loginfrm(self):
        self.Frame_login= Frame(self.root,bg="#F5F5F5")
        self.Frame_login.place(x=350,y=150,height=340,width=400)

        load =Image.open(r"D:\phython\FMS\FLIGHT-BOOKING-SYSTEM-OPEN-CV-\login1.png")
        load= load.resize((100, 100),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        
        img = Label(self.Frame_login,image=render,bg="#F5F5F5")
        img.image= render
        img.place(x=0,y=10) 
        

        user=Label(self.Frame_login,text="User name",font=("Candara Bold",15,),fg="black",bg="white").place(x=0,y=120)
        self.text_user=Entry(self.Frame_login,font=("times new roman",15),bg="lightblue")
        self.text_user.place(x=10,y=150,width=300,height=35)


        passw=Label(self.Frame_login,text="password",font=("Candara Bold",15,"bold"),fg="black",bg="white").place(x=0,y=210)
        self.text_passw=Entry(self.Frame_login,font=("times new roman",15),bg="lightblue",show="*")
        self.text_passw.place(x=10,y=240,width=300,height=35)

        login= Button(self.Frame_login,text="LOGIN",bg="white",fg="#C0C0C0",font=("Candara Bold",25),bd=0,command=self.loginfun ).place(x=230,y=280,height=40,width=140)



    @staticmethod
    def setting():
            def Delete(event):
                el.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                row_id =listBox.selection()[0]
                select =listBox.set(row_id)
                e1.insert(0,select['id'])
                e2.insert(0,select['stname'])
                e3.insert(0,select['course'])
                e4.insert(0,select['fee'])

            def add():
                flightcode = e1.get()
                source = e2.get()
                destination = e3.get()
                no_of_seats = e4.get()

                mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest')
                mycursor= mysqldb.cursor()      

                try:
                    sql ="insert into flight (FLIGHT_CODE,SOURCE,DESTINATION,NO_OF_SEATS) values(%s,%s,%s,%s)"
                    val =(flightcode,source,destination,no_of_seats)
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    lsatid= mycursor.lastrowid
                    messagebox.showinfo("information","record inserted  successfully....")
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    e4.delete(0,END)
                    e1.focus_set()

                except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()
           
            def update():
                    flightcode = e1.get()
                    source =e2.get()
                    destination =e3.get()
                    no_of_seats = e4.get()


                    mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest',)
                    mycursor= mysqldb.cursor()       
                    try:
                        sql ="UPDATE flight SET SOURCE=%s,DESTINATION=%s,NO_OF_SEATS=%s,where FLIGHT_CODE=%s"
                        val =(source,destination,no_of_seats,flightcode)
                        mycursor.execute(sql,val)
                        mysqldb.commit()
                        lsatid= mycursor.lastrowid
                        messagebox.showinfo("information","record updated  successfully....")
                        e1.delete(0,END)
                        e2.delete(0,END)
                        e3.delete(0,END)
                        e4.delete(0,END)
                        e1.focus_set()

                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

            def delete():
                flightcode = e1.get()

                mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest',)
                mycursor= mysqldb.cursor()    
                try:
                    sql ="delete from flight where FLIGHT_CODE =%s"
                    val =(flightcode,)
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    lsatid= mycursor.lastrowid
                    messagebox.showinfo("information","record deleted  successfully....")
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    e4.delete(0,END)
                    e1.focus_set()

                except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()

            def show():
                studid = e1.get()

                mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest',)
                mycursor= mysqldb.cursor()     
       
                mycursor.execute("select FLIGHT_CODE,SOURCE,DESTINATION,NO_OF_SEATS,price FROM flight")
                records = mycursor.fetchall()
                # print(records)

                for i, (FLIGHT_CODE,SOURCE,DESTINATION,NO_OF_SEATS,price) in enumerate(records,start=1):
                    listBox.insert("","end", values = (FLIGHT_CODE,SOURCE,DESTINATION,NO_OF_SEATS,price))
                    mysqldb.close()

            
            root1=Toplevel()
            root1.title('Admin')
            
            root1.resizable(False,False)
            adimage =Image.open("D:\phython\FMS\cover.jpg")
            adimage = adimage.resize((1100, 600),Image.ANTIALIAS)
            photo =ImageTk.PhotoImage(adimage)
            w= photo.width()
            h=photo.height()
            root1.geometry('%dx%d+0+0'%(w,h))
            labelText = StringVar()
            labelText.set("welcome !!!")

            label1 = Label(root1,image=photo,textvariable=labelText,font=("Times New Roman",24),justify=CENTER,height=4,fg="blue")
            label1.place(x=0,y=0,relwidth=1,relheight=1)
            global e1
            global e2
            global e3

            Label(root1,text="FLIGHT'S SETTING" ,fg="black",font=(None,30)).place(x=400,y=5)

            Label(root1,text="FLIGHT_CODE").place(x=10,y=10)

            Label(root1,text="SOUCRE").place(x=10,y=40)

            Label(root1,text="DESTINATION").place(x=10,y=70)

            Label(root1,text="NO_OF_SEATS").place(x=10,y=100)
            e1 =Entry(root1)
            e1.place(x=140,y=10)
            e2=Entry(root1)
            e2.place(x=140,y=40)
            e3=Entry(root1)
            e3.place(x=140,y=70)
            e4=Entry(root1)
            e4.place(x=140,y=100)
            Button(root1,text="ADD",command=add,height=3,width=13).place(x=30,y=130)
            Button(root1,text="UPDATE",command=update,height=3,width=13).place(x=140,y=130)
            Button(root1,text="DELETE",command=delete,height=3,width=13).place(x=250,y=130)
            cols =('FLIGHT_CODE','SOURCE','DESTINATION','NO_OF_SEATS')
            listBox = ttk.Treeview(root1,columns=cols,show='headings')

            for col in cols:
                listBox.heading(col,text=col)
                listBox.grid(row=1,column=0,columnspan=2)
                listBox.place(x=10,y=200)

            show()
            listBox.bind('<Double-Button-1>',delete)
            root1.mainloop()
  
    def loginfun(self):
       
        if self.text_passw.get()=="" or self.text_user.get()=="":
            messagebox.showerror("ERROR","ALL FIELDS ARE  REQUIRED",parent=self.root)
        elif self.text_passw.get()!="admin" or self.text_user.get()!="admin":
            messagebox.showerror("ERROR","invalid INPUT",parent=self.root)
        else:
            self.ico =Image.open(r"D:\phython\FMS\FLIGHT-BOOKING-SYSTEM-OPEN-CV-\colck2.jpg")

            self.ico = self.ico.resize((1100, 600),Image.ANTIALIAS)
            self.photo =ImageTk.PhotoImage(self.ico)
            self.root.iconphoto(False,self.photo)
            self.bg_image=Label(self.root,image=self.photo).place(x=0,y=0,relwidth=1,relheight=1)
            # messagebox.showinfo("welome",f"{self.text_user.get()}",parent=self.root)

            self.Frame_login.destroy()
            # self.Frame_login1.destroy()
            clock_label = Label(root,bg="black",fg='white',font=("Impact",25))
            clock_label.place(x=450,y=0,height=120,width=520)

            def update_label():
                curr=strftime('%H: %M: %S')
                clock_label.configure(text=curr)
                clock_label.after(80,update_label)
            update_label()

            menubar= Menu(self.root)
            filemenu= Menu(menubar,tearoff=0)
            filemenu.add_command(label="BOOK TICKET",command=self.book_ticket) 
            
            filemenu.add_command(label="CANCEL TICKET",command=self.cancel_ticket)  
            filemenu.add_command(label="SETTING",command=login.setting)  
            filemenu.add_separator() 
            filemenu.add_command(label="EXIT",command=root.quit)
            menubar.add_cascade(label=u'\u2630',menu=filemenu)

            self.root.config(menu=menubar)
            
    def  cancel_ticket(self):
              
        def delete():

                ticketcode = tkc.get()

                mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest',)
                mycursor= mysqldb.cursor()    
                try:
                    sql ="delete from passenger where ticket_code =%s"
                    val =(ticketcode,)
                    mycursor.execute(sql,val)
                    mysqldb.commit()
                    lsatid= mycursor.lastrowid
                    messagebox.showinfo("information","record deleted  successfully....")
                    tkc.delete(0,END)
                    tkc.focus_set()

                except Exception as e:
                    print(e)
                    mysqldb.rollback()
                    mysqldb.close()
        root12=Tk()
        root12.title("cancel ticket window")
        root12.configure(bg="black")
        

        tkcode=Label(root12,text="enter your ticket id ").place(x=20,y=20)
        tkc=Entry(root12)
        tkc.place(x=20,y=50)

        bt=Button(root12,text="DELETE",command=delete).place(x=0,y=90)         
  
    def book_ticket(self):
            self.root.title("book ticket")
            self.Frame_booking= Frame(self.root,bg="#2F4F4F")
            self.Frame_booking.place(x=150,y=150,height=400,width=800)
            global source
            global destination
            global cal
            global variable1
            global variable2
            global variable3
            
            
            Label(self.Frame_booking,text="Search Flights",font=("Candara Bold",25,"bold"),fg="#C0C0C0",bg="#F5F5F5").place(x=180,y=0,width=400)
            
            Label(self.Frame_booking,text="FROM",font=("Candara Bold",12),bg="#C0C0C0",fg="black").place(x=50,y=60,width=50)
            source=Entry(self.Frame_booking,font=("times new roman",15),bg="lightblue")
            source.place(x=100,y=60,height=24,width=100)

            Label(self.Frame_booking,text="TO",font=("Candara Bold",12),bg="#C0C0C0",fg="black").place(x=50,y=110,width=50)
            destination=Entry(self.Frame_booking,font=("times new roman",15),bg="lightblue")
            destination.place(x=100,y=110,height=24,width=100)

            Label(self.Frame_booking,text='DATE',font=("Candara Bold",12),bg="#C0C0C0",fg="black").place(x=50,y=160,width=50)
            cal=DateEntry(self.Frame_booking,width=16,bg="lightblue",fg="black",)
            cal.place(x=100,y=160,height=24,width=100)

            variable1 = StringVar(self.Frame_booking)
            Label(self.Frame_booking,text="ADULT(+12)").place(x=50,y=210)
            variable1.set(0) 
            w = OptionMenu(self.Frame_booking, variable1, "0","1", "2", "3","4","5")
            w.configure(fg="black",font=("Candara Bold",12),bg='#C0C0C0')
            w.place(x=50,y=250)
                        
            variable3 = StringVar(self.Frame_booking)
            
            Label(self.Frame_booking,text="childern(+6)").place(x=190,y=210)
            variable3.set(0) 
            w = OptionMenu(self.Frame_booking, variable3, "0","1", "2", "3","4","5")
            w.configure(fg="black",font=("Candara Bold",12),bg='#C0C0C0')
            w.place(x=190,y=250)

            variable2= StringVar(self.Frame_booking)
            variable2.set("CLASS")
            w = OptionMenu(self.Frame_booking, variable2, "BUSSINESSS","ECONOMY","FIRST CLASS")
            w.configure(fg="black",font=("algerian",12),bg='#C0C0C0')
            w.place(x=390,y=250)
            
            btn=Button(self.Frame_booking,text="Get Set Go",bg="#F5F5F5",font=("Impact",12),command=self.Flight_details).place(x=180,y=300,height=40,width=400)

    def Flight_details(self):

        
        self.Frame_booking= Frame(self.root,bg="#2F4F4F")
        self.Frame_booking.place(x=150,y=150,height=400,width=800)
        global k
        
        k=1
        while k==1:
            if source.get()=="" or destination.get()=="":
                messagebox.showerror("ERROR","ALL FIELDS ARE  REQUIRED",parent=self.root)
                break
                

            else:
                Label(self.Frame_booking,text=" AVAILABLE FLIGHT'S ",bg='#C0C0C0',fg='yellow',font=("Impact",30) ).place(x=90,y=0)
                global FC
                FC=0
                Label(self.Frame_booking,text="SELECT FLIGHT CODE").place(x=10,y=100)
                FC=Entry(self.Frame_booking,font=("times new roman",15),bg="white")
                FC.place(x=150,y=100,width=100)

                def show():
                    s=source.get()
                    d=destination.get()
                    mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest',)
                    mycursor= mysqldb.cursor()     
       
                    mycursor.execute(f"SELECT * from flight where SOURCE='{s}' and DESTINATION='{d}'")
                    records = mycursor.fetchall()

                    for i, (FLIGHT_CODE,SOURCE,DESTINATION,NO_OF_SEATS,price) in enumerate(records,start=1):
                        listBox.insert("","end", values = (FLIGHT_CODE,SOURCE,DESTINATION,NO_OF_SEATS,price))
                    mysqldb.close()

                cols =('FLIGHT_CODE','SOURCE','DESTINATION','NO_OF_SEATS','price')


                listBox = ttk.Treeview(self.Frame_booking,columns=cols,show='headings')

                for col in cols:
                    listBox.heading(col,text=col)
                    listBox.column(col,minwidth=0,width=100)
                    listBox.grid(row=1,column=0,columnspan=2)
                    listBox.place(x=10,y=130)   

                show()
                bn=Button(self.Frame_booking,text="CONTINUE",bg="orange",font=("Impact",12),command=self.passenger_details)
                bn.place(x=300,y=100,height=24,width=200)
                k=0

    def passenger_details(self):
        
        self.root.title("book ticket")    
        self.Frame_booking= Frame(self.root,bg="#2F4F4F")
        self.Frame_booking.place(x=150,y=150,height=400,width=800)

        self.Frame_booking1= Frame(self.Frame_booking,bg="#C0C0C0")
        self.Frame_booking1.place(x=500,y=30,height=200,width=200)

        F=destination.get()
        T=source.get()
        D=cal.get()
        NO_A=variable1.get()
        NO_C=variable3.get()
        CLASS=variable2.get()
        fc=FC.get()

        total_pessangers=int(NO_A) + int(NO_C)
        def show():
                    global amount
                    amount=1
                    FLC=FC.get()
                    mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest',)
                    mycursor= mysqldb.cursor()
                    sql=f"SELECT price from flight where FLIGHT_CODE='{FLC}'"     
                    mycursor.execute(sql)
                    records = mycursor.fetchall()
                    i=0
                    for value in records:
                        amount=records[0][0]
                    i=i+1
                    print()  
        show()    
        global total        
        total =total_pessangers*amount 
        Label(self.Frame_booking1,text="TICKET INFO",font=("Impact",12),fg="black",bg="#C0C0C0").place(x=50,y=0)
        Label(self.Frame_booking1,text=f"FROM {F} TO {T}",font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=10,y=30)
        Label(self.Frame_booking1,text=D,font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=10,y=60)
        Label(self.Frame_booking1,text=fc,font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=10,y=90)
        Label(self.Frame_booking1,text=f"number of passanger {total_pessangers} ",font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=10,y=120)
        
        Label(self.Frame_booking1,text=f"AMOUNT {total}  rs ",font=("Candara Bold",15),fg="orange",bg="green").place(x=10,y=150)

        global p_fname
        global p_lname
        global p_age
        global p_phone
        global p_email
        global p_address
        global p_tkcode


        Label(self.Frame_booking,text="PASSENGER DETAILS",font=("Impact",25,"bold"),fg="#C0C0C0",bg="#2F4F4F").place(x=90,y=10)
        Label(self.Frame_booking,text="FIRST NAME :-",font=("Candara Bold",12),fg="#d77337",bg="#2F4F4F").place(x=50,y=60)
        Label(self.Frame_booking,text="LAST NAME :-",font=("Candara Bold",12),fg="#d77337",bg="#2F4F4F").place(x=50,y=120)
        Label(self.Frame_booking,text="AGE :-",font=("Candara Bold",12),fg="#d77337",bg="#2F4F4F").place(x=50,y=180)
        Label(self.Frame_booking,text="PHONE :-",font=("Candara Bold",12),fg="#d77337",bg="#2F4F4F").place(x=50,y=240)        
        Label(self.Frame_booking,text="EMAIL :-",font=("Candara Bold",12),fg="#d77337",bg="#2F4F4F").place(x=50,y=300)
        Label(self.Frame_booking,text="ADDRESS :-",font=("Candara Bold",12),fg="#d77337",bg="#2F4F4F").place(x=50,y=360)
        Label(self.Frame_booking,text="TICKET CODE :-",font=("Candara Bold",12),fg="#d77337",bg="#2F4F4F").place(x=500,y=240)

        p_fname=Entry(self.Frame_booking,text="FIRST NAME")
        p_fname.place(x=150,y=60,width=100)
        p_lname=Entry(self.Frame_booking,text="LAST NAME")
        p_lname.place(x=150,y=120,width=100)
        p_age=Entry(self.Frame_booking,text="AGE")
        p_age.place(x=150,y=180,width=100)
        p_phone=Entry(self.Frame_booking,text="PHONE NUMBER")
        p_phone.place(x=150,y=240,width=100)
        p_email=Entry(self.Frame_booking,text="EMAIL")
        p_email.place(x=150,y=300,width=100)
        p_address=Entry(self.Frame_booking,text="ADDRESS")
        p_address.place(x=150,y=360,width=100)  
        p_tkcode=Entry(self.Frame_booking,text="ticket code")
        p_tkcode.place(x=500,y=240,width=100)  
        
        PHOTO=Button(self.Frame_booking,text="PHOTO",command=self.photos,bg="#C0C0C0").place(x=300,y=360)
        BTN=Button(self.Frame_booking,text="CONTINUE",command=self.ticket,bg="#C0C0C0").place(x=700,y=360)
      
    def ticket(self):
        ico =Image.open("D:\phython\FMS\main1.jpg")
        photo =ImageTk.PhotoImage(ico)
        root.iconphoto(False,photo)
        self.root.title("book ticket")    
        self.Frame_booking= Frame(self.root,bg="#2F4F4F")
        self.Frame_booking.place(x=150,y=150,height=400,width=800)
        k=1
        while k==1:
            if p_fname.get()==" " or p_lname.get()==" ":
                messagebox.showerror("ERROR","ALL FIELDS ARE  REQUIRED",parent=self.root)

            elif p_age.get()==" " or p_phone.get()==" ":
                messagebox.showerror("ERROR","ALL FIELDS ARE  REQUIRED",parent=self.root)
            else:

                def add():
                
                    f = p_fname.get()
                    l = p_lname.get()
                    ae = p_age.get()
                    ph = p_phone.get()
                    em = p_email.get()
                    ad = p_address.get()
                    tkc = p_tkcode.get()

                    mysqldb=connector.connect(host='localhost',
                                    port='3306',
                                    user='root',
                                    password='1234',
                                    database='flighttest')
                    mycursor= mysqldb.cursor()      

                    try:
                        sql =f"insert into passenger values('{f}','{l}',{ae},{ph},'{em}','{ad}',{tkc})"
                        mycursor.execute(sql)
                        mysqldb.commit()
                        lsatid= mycursor.lastrowid
                        messagebox.showinfo("information","record inserted  successfully....")
                    
                        p_fname.focus_set()

                    except Exception as e:
                        print(e)
                        mysqldb.rollback()
                        mysqldb.close()

                add()
                self.Frame_booking1= Frame(self.Frame_booking,bg="#C0C0C0")
                self.Frame_booking1.place(x=10,y=20,height=500,width=600)

                F=destination.get()
                T=source.get()
                D=cal.get()
                NO_A=variable1.get()
                NO_C=variable3.get()
                CLASS=variable2.get()
                fc=FC.get()
        
                total_pessangers=int(NO_A) + int(NO_C)    

                f = p_fname.get()
                l = p_lname.get()
                ae = p_age.get()
                ph = p_phone.get()
                em = p_email.get()
                ad = p_address.get()                    
        
        
                Label(self.Frame_booking1,text="TICKET SUMMARY",font=("Impact",25),fg="black",bg="#C0C0C0").place(x=50,y=0)
        
                Label(self.Frame_booking1,text=f"NAME :- {f}  {l}",font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=150,y=50)
        
                Label(self.Frame_booking1,text=ae,font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=300,y=50)
        
                Label(self.Frame_booking1,text=f"FROM {F} TO {T} ",font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=150,y=100)
        
                Label(self.Frame_booking1,text=f" DATE {D} ",font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=150,y=150)
        
                Label(self.Frame_booking1,text=f" FLIGHT CODE {fc}",font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=150,y=200)
        
                Label(self.Frame_booking1,text=f"TOTAL PASSANGER {total_pessangers} ",font=("Candara Bold",12),fg="black",bg="#C0C0C0").place(x=0,y=300)
        
                Label(self.Frame_booking1,text=f"AMOUNT {total}  rs ",font=("Candara Bold",15),fg="orange",bg="green").place(x=0,y=330)

                load =Image.open('D:\phython\FMS\{}.png'.format(f))
                load= load.resize((90, 90),Image.ANTIALIAS)
                render = ImageTk.PhotoImage(load)
        
                img = Label(self.Frame_booking1,image=render,bg="#2F4F4F")
                img.image= render
                img.place(x=10,y=50)
                bt=Button(self.Frame_booking1,text="PAY CASH",command=self.root.quit)
                bt.place(x=300,y=330)
                k=0
        

    def photos(self):
            print("photos also impoted")
            cam=cv2.VideoCapture(0)
            cv2.namedWindow("passenger photo")
            n=p_fname.get()
            while True:
                check,frame = cam.read()
                if not check:
                    print("technical  error")
                    break

                cv2.imshow("PHOTO",frame)
                k = cv2.waitKey(1)
                if k%256 == 27:
                    print("thank you")
                    break
                elif k%256 ==32 :
                    img_name ="D:\phython\FMS\{}.png".format(n)
                    cv2.imwrite(img_name,frame)

                    print("photo have been taken ,you can close by ESC") 
            cam.release()
root=Tk()
obj=login(root)
root.mainloop()