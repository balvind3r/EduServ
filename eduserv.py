from tkinter import *
import pyfiglet
import mysql.connector
con=mysql.connector.connect(host='localhost',password='BRAIN',user='root')
cur=con.cursor()

#==============================CREATING DB=====================================
cur.execute('create database if not exists pyschool')
con.commit() 
cur.execute('use pyschool')
con.commit() 
cur.execute('create table if not exists pystudent(ADMISSION_NUMBER varchar(50) NOT NULL, NAME VARCHAR(25) NOT NULL, GENDER VARCHAR(1),CLASS CHAR(10),DOB VARCHAR(50))')
con.commit() 

def add_record():
    root=Tk()
    root.title('ADD RECORD')
    root.geometry('720x720+0+0')
    Frame(root,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=720)
    Label(root,text='ADD NEW RECORD',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #===========================ADM NO.================================
    Label(root,text='ADMISSION NUMBER ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    adm_no=StringVar()
    Entry(root,textvariable=adm_no,width=25,bg='white').place(x=400,y=161)
    

    #==========================NAME====================================
    Label(root,text='NAME ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=250)
    name=StringVar()
    Entry(root,textvariable=name,width=25,bg='white').place(x=400,y=250)

    #=========================GENDER===================================
    Label(root,text='GENDER ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=350)
    gen=StringVar()
    Radiobutton(root, text="MALE",variable=gen,value="M").place(x=400,y=350)
    Radiobutton(root, text="FEMALE",variable=gen,value="F").place(x=480,y=350)

    #=========================CLASS====================================
    Label(root,text='CLASS ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=450)
    class_list=('I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII')
    clss=StringVar()
    OptionMenu(root,clss,*class_list).place(x=400,y=450)    

    #========================DOB=======================================
    Label(root,text='DATE OF BIRTH ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=550)
    date_list=('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
    month_list=('JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER')
    year_list=('2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020')
    date=StringVar()
    month=StringVar()
    year=StringVar()
    OptionMenu(root,date,*date_list).place(x=400,y=550)
    OptionMenu(root,month,*month_list).place(x=450,y=550)
    OptionMenu(root,year,*year_list).place(x=540,y=550)
    
    def do_it():
        an=str(adm_no.get()).upper()
        nm=str(name.get()).upper()
        g=str(gen.get()).upper()
        cl=str(clss.get())
        db=str(date.get())+' '+str(month.get())+' '+str(year.get())
        cur.execute("insert into pystudent values('{}','{}','{}','{}','{}')".format(an,nm,g,cl,db))
        con.commit()
        print(' '*242+'Record Added Successfully...')
          
   
    Button(root,text='ADD',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()

def show_data():
    cur.execute('select * from pystudent')
    data=cur.fetchall()
    for i in data:
        print(i)

def update_data():
    
    root=Tk()
    root.title('UPDATE DATA')
    root.geometry('720x600+0+0')
    Frame(root,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=600)
    Label(root,text='UPDATE RECORD',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #===========================ADM NO.================================
    Label(root,text='ADMISSION NUMBER ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    adm_no=StringVar()
    Entry(root,textvariable=adm_no,width=25,bg='white').place(x=400,y=161)
    

    #=========================CLASS====================================
    Label(root,text='CLASS ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=250)
    class_list=('NO CHANGE','I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII')
    clss=StringVar()
    OptionMenu(root,clss,*class_list).place(x=400,y=250)    

    #========================DOB=======================================
    Label(root,text='DATE OF BIRTH ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=350)
    date_list=('NO CHANGE','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31')
    month_list=('NO CHANGE','JANUARY','FEBRUARY','MARCH','APRIL','MAY','JUNE','JULY','AUGUST','SEPTEMBER','OCTOBER','NOVEMBER','DECEMBER')
    year_list=('NO CHANGE','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018','2019','2020')
    date=StringVar()
    month=StringVar()
    year=StringVar()
    OptionMenu(root,date,*date_list).place(x=400,y=350)
    OptionMenu(root,month,*month_list).place(x=480,y=350)
    OptionMenu(root,year,*year_list).place(x=560,y=350)
    
    def do_it():
        an=str(adm_no.get()).upper()
        cl=str(clss.get())
        db=str(date.get())+' '+str(month.get())+' '+str(year.get())
        if cl != 'NO CHANGE':
            cur.execute("update pystudent set CLASS=('{}') where ADMISSION_NUMBER=('{}') ".format(cl,an))
            con.commit()
        if 'NO CHANGE' not in db :
            cur.execute("update pystudent set DOB =('{}') where ADMISSION_NUMBER=('{}') ".format(db,an))
            con.commit()
        print(' '*242+'Updation Successful...')           
    
    Button(root,text='UPDATE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()

def delete_data():
    root=Tk()
    root.title('DELETE DATA')
    root.geometry('500x500+0+0')
    Frame(root,bd=4,relief=RIDGE,bg='cyan').place(x=0,y=0,width=720,height=600)
    Label(root,text='DELETE RECORD',bd=10,relief=GROOVE,font=('times new roman',40,'bold'),bg='yellow',fg='red').pack(side=TOP,fill=X)
    
    #===========================ADM NO.================================
    Label(root,text='ADMISSION NUMBER ',bg='cyan',fg='black',font=('arial',20,'bold')).place(x=30,y=150)
    adm_no=StringVar()
    Entry(root,textvariable=adm_no,width=25,bg='white').place(x=325,y=161)

    def do_it():
        an=str(adm_no.get()).upper()
        cur.execute("delete from pystudent where ADMISSION_NUMBER=('{}') ".format(an))
        con.commit()
        print(' '*242+'Deletion Successful...')           
    
    Button(root,text='DELETE',bd=10,relief=GROOVE,bg='lightblue',fg='navy blue',font=('times new roman',40,'bold'),command=do_it).pack(side=BOTTOM, fill=X)
    
    root.mainloop()


while True:
    print(pyfiglet.figlet_format('WELCOME TO EDUSERV',font='speed'))
    print('*'*501)
    print('MAIN MENU'.center(501))
    print('1. Enter New Data'.center(501))
    print('2. Display Existing Data'.center(501))
    print('3. Update Existing Record'.center(501))
    print('4. Delete Existing Record'.center(501))
    print('5. EXIT'.center(501))
    
    print('*'*501)
    ch=int(input(' '*242+'Enter your Choice: '))
    if ch==1:
        add_record()
    if ch==2:
        show_data()
    if ch==3:
        update_data()
    if ch==4:
        delete_data()
    if ch==5:
        break
