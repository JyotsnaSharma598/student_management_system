import MySQLdb
from Tkinter import *
import tkMessageBox
from PIL import ImageTk,Image
import os


conn = MySQLdb.connect("localhost","root","","project")

cur = conn.cursor()

root = Tk()
root.geometry("1350x750+1+1")
root.title("Information System")
root.configure(background='blue')

Tops=Frame(root,width=1650,height=100,bd=16,relief="raise")
Tops.pack(side=TOP)

f1=Frame(root,width=500,height=600,bd=16,relief="raise")
f1.pack(side=LEFT)
f2=Frame(root,width=500,height=600,bd=8,relief="raise")
f2.pack(side=RIGHT)
#f3=Frame(root,width=500,height=500,bd=8,relief="raise")
#f3.pack(side=RIGHT)

f1aa=Frame(f1,width=500,height=600,bd=16,relief="raise")
f1aa.grid(row=0,padx=10)
f1ab=Frame(f2,width=500,height=600,bd=16,relief="raise")
f1ab.grid(row=0,padx=10)
#f1ab.grid_propagate(0)
#f1ac=Frame(f3,width=500,height=500,bd=16,relief="raise")
#f1ac.grid(row=0,padx=10)


def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()

def exitw() :
    root = Tk()
    y = 'good bye!'
    tkMessageBox.showinfo('demo',y)
    root.mainloop()
    exit()

def make_button():
    b = Button(f1aa)
    image = ImageTk.PhotoImage(file="app.jpg")
    b.config(image=image,command=student)
    b.image = image
    b.grid(row=1,column=0)
    #l = Label(f1aa,font=('arial',14,'bold'), text=' STUDENT ')
    #l.grid(row=2,column=0)

def make_button2():
    b = Button(f1ab)
    image = ImageTk.PhotoImage(file="teacher.jpg")
    b.config(image=image,command=admin)
    b.image = image
    b.grid(row=1,column=0)
    #l = Label(f1aa,font=('arial',14,'bold'),text=' TEACHER ')
    #l.grid(row=4,column=0) 


    
 
def verifyl(name_entry,password):
    name = name_entry.get()
    password = password.get()
    x = cur.execute('SELECT * FROM users_stu WHERE form_no=%s and password=%s',(name, password))
    if x:
        x='permission granted '
        tkMessageBox.showinfo('Demo',x)
        root = Tk()
        root.geometry("1350x750+1+1")
        root.title("Information System")
        root.configure(background='blue')
        Tops=Frame(root,width=1650,height=100,bd=16,relief="raise")
        Tops.pack(side=TOP)
        Tops.pack_propagate(0)
        f1=Frame(root,width=250,height=700,bd=16,relief="raise")
        f1.pack(side=LEFT)
        f2=Frame(root,width=900,height=700,bd=16,relief="raise")
        f2.pack(side=RIGHT)

        f1aa=Frame(f1,width=250,height=700,bd=16,relief="raise")
        f1aa.grid(row=0,padx=10)
        f1aa.grid_propagate(0)
        f1ab=Frame(f2,width=900,height=700,bd=16,relief="raise")
        f1ab.grid(row=0,padx=10)
        f1ab.grid_propagate(0)
        def details(name_entry):
             name = name_entry.get()
             x = cur.execute('SELECT * from student WHERE form_no=%s',[name])
             Label(f1ab,font=('arial',18,'bold'),text="DETAILS").grid(row=1,column=2)
             Label(f1ab,font=('arial',16,'bold'),text="NAME: ").grid(row=2,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="PHONE: ").grid(row=3,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="E-MAIL: ").grid(row=4,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="COURSE: ").grid(row=5,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="MOTHER NAME: ").grid(row=6,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="FATHER NAME: ").grid(row=7,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="ADDRESS: ").grid(row=8,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="FORM NO.: ").grid(row=9,column=1)
             Label(f1ab,font=('arial',16,'bold'),text="ENROLLMENT NO.: ").grid(row=10,column=1)
             i = 2
             j = 2
             for x in cur:
                  a1 = Label(f1ab,font=('arial',14,'bold'),text=x[0]).grid(row=i,column=j)
                  a2 = Label(f1ab,font=('arial',14,'bold'),text=x[1]).grid(row=i+1,column=j)
                  a3 = Label(f1ab,font=('arial',14,'bold'),text=x[2]).grid(row=i+2,column=j)
                  a4 = Label(f1ab,font=('arial',14,'bold'),text=x[3]).grid(row=i+3,column=j)
                  a5 = Label(f1ab,font=('arial',14,'bold'),text=x[4]).grid(row=i+4,column=j)
                  a6 = Label(f1ab,font=('arial',14,'bold'),text=x[5]).grid(row=i+5,column=j)
                  a7 = Label(f1ab,font=('arial',14,'bold'),text=x[6]).grid(row=i+6,column=j)
                  a8 = Label(f1ab,font=('arial',14,'bold'),text=x[7]).grid(row=i+7,column=j)
                  a9 = Label(f1ab,font=('arial',14,'bold'),text=x[8]).grid(row=i+8,column=j)
                  i = i + 1
    
        y = cur.execute('SELECT name FROM users_stu WHERE form_no=%s and password=%s',(name, password))
        for y in cur:
            z = Label(Tops,font=('arial',16,'bold'),text='welcome ',width=10).grid(row=1,column=0)
            a = Label(Tops,font=('arial',16,'bold'),text=y,width=25).grid(row=1,column=1)
            q = Button(Tops,text="Logout",command= lambda: exitw()).grid(row=1,column=14)

 
        def attendence(name_entry):
            name = name_entry.get()
            x = cur.execute('SELECT code,sub_name,no_of_credits,attendence from subject WHERE form_no=%s',[name])
            Label(f1ab,font=('arial',18,'bold'),text="ATTENDENCE").grid(row=0,column=2)
            Label(f1ab,font=('arial',16,'bold'),text='subject code').grid(row=1,column=0)
            Label(f1ab,font=('arial',16,'bold'),text='subject name').grid(row=1,column=1)
            Label(f1ab,font=('arial',16,'bold'),text='no. of credits').grid(row=1,column=2)
            Label(f1ab,font=('arial',16,'bold'),text='attendence').grid(row=1,column=3)
            i = 2
            j = 0
            for x in cur:
                  a1 = Label(f1ab,font=('arial',14,'bold'),text=x[0]).grid(row=i,column=j)
                  a2 = Label(f1ab,font=('arial',14,'bold'),text=x[1]).grid(row=i,column=j+1)
                  a3 = Label(f1ab,font=('arial',14,'bold'),text=x[2]).grid(row=i,column=j+2)
                  a4 = Label(f1ab,font=('arial',14,'bold'),text=x[3]).grid(row=i,column=j+3)
                  i = i + 1
    
        def faculty(name_entry):
            name = name_entry.get()
            x = cur.execute('SELECT professor_name,email,phone,post from faculty WHERE form=%s',[name])
            Label(f1ab,font=('arial',18,'bold'),text="FACULTY").grid(row=0,column=2)
            Label(f1ab,font=('arial',16,'bold'),text='Professor').grid(row=1,column=0)
            Label(f1ab,font=('arial',16,'bold'),text='E-mail').grid(row=1,column=1)
            Label(f1ab,font=('arial',16,'bold'),text='Phone No.').grid(row=1,column=2)
            Label(f1ab,font=('arial',16,'bold'),text='Post').grid(row=1,column=3)
            i = 2
            j = 0
            for x in cur:
                a1 = Label(f1ab,font=('arial',14,'bold'),text=x[0]).grid(row=i,column=j)
                a2 = Label(f1ab,font=('arial',14,'bold'),text=x[1]).grid(row=i,column=j+1)
                a3 = Label(f1ab,font=('arial',14,'bold'),text=x[2]).grid(row=i,column=j+2)
                a4 = Label(f1ab,font=('arial',14,'bold'),text=x[3]).grid(row=i,column=j+3)
                i = i + 1

        def marksheet(name_entry):
            name = name_entry.get()
            x = cur.execute('SELECT sub_name,no_of_credits,marks from subject WHERE form_no=%s',[name])
            Label(f1ab,font=('arial',18,'bold'),text="MARKSHEET").grid(row=1,column=2)
            Label(f1ab,font=('arial',16,'bold'),text="Subject").grid(row=2,column=1)
            Label(f1ab,font=('arial',16,'bold'),text="Credits").grid(row=2,column=2)
            Label(f1ab,font=('arial',16,'bold'),text="Marks").grid(row=2,column=3)
            i = 3
            j = 1
            for x in cur:
                a1 = Label(f1ab,font=('arial',14,'bold'),text=x[0]).grid(row=i,column=j)
                a2 = Label(f1ab,font=('arial',14,'bold'),text=x[1]).grid(row=i,column=j+1)
                a3 = Label(f1ab,font=('arial',14,'bold'),text=x[2]).grid(row=i,column=j+2)
    
        b1=Button(f1aa,font=('arial',12,'bold'),text="attendence",height=2,width=20,command= lambda: attendence(name_entry)).grid(row=1,column=0)
        b2=Button(f1aa,font=('arial',12,'bold'),text="details",height=2,width=20,command= lambda: details(name_entry)).grid(row=2,column=0)
        b3=Button(f1aa,font=('arial',12,'bold'),text="marksheet",height=2,width=20,command= lambda: marksheet(name_entry)).grid(row=3,column=0)
        b4=Button(f1aa,font=('arial',12,'bold'),text="faculty",height=2,width=20,command= lambda: faculty(name_entry)).grid(row=4,column=0)
        root.mainloop()
    else:
        y = 'permission denied'
        tkMessageBox.showinfo('demo',y)
        exit()




def lstudent():
    root = Tk()
    l = Label(root, text='_+_+_+_+ WELCOME TO LOGIN WINDOW, STUDENT_+_+_+_+_').grid(row=1)
    
    l1 = Label(root, text='form number:',width=25).grid(row=2,column=0)
    name_entry = Entry(root)
    name_entry.grid(row=2,column=1)
    
    l2 = Label(root, text='password:',width=25).grid(row=3,column=0)
    password = Entry(root,show='*')
    password.grid(row=3,column=1)

    b1=Button(root,text="LOGIN",command= lambda: verifyl(name_entry,password)).grid(row=4,column=0)
       
    root.mainloop()
 

    
def student():
    
    l = Label(f1aa,font=('arial',14,'bold'), text=' WELCOME STUDENT ')
    l.grid(row=2,column=0)

    l1 = Label(f1aa,font=('arial',14,'bold'),text='User Name:',width=25).grid(row=3,column=0)
    name_entry = Entry(f1aa)
    name_entry.grid(row=3,column=1)
    
    l2 = Label(f1aa,font=('arial',14,'bold'),text='Password:',width=25).grid(row=4,column=0)
    password = Entry(f1aa,show='*')
    password.grid(row=4,column=1)

    b1=Button(f1aa,font=('arial',12,'bold'),text="LOGIN",command= lambda: verifyl(name_entry,password)).grid(row=5,column=0)
    name_entry.delete(0,END)
    password.delete(0,END)

           
def input_record2(name_entry,phone_entry,email_entry,course_entry,mn_entry,fn_entry,address_entry,form_no_entry,enrollment_no_entry):
            
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    course = course_entry.get()
    mn = mn_entry.get()
    fn = fn_entry.get()
    address = address_entry.get()
    form_no = form_no_entry.get()
    enrollment_no = enrollment_no_entry.get()
    cur.execute("INSERT INTO student (name,phone,email,course,mother_name,father_name,address,form_no,enrollment_no) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name,phone,email,course,mn,fn,address,form_no,enrollment_no))
    conn.commit()
    x='information stored '
    tkMessageBox.showinfo('Demo',x)
    exit()



    

def edit_record2(name_entry,phone_entry,email_entry,course_entry,mn_entry,fn_entry):
    name = mn_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    course = course_entry.get()
    address = fn_entry.get()
    en = name_entry.get()
    y = cur.execute('UPDATE student SET phone=%s,address=%s,email=%s,course=%s,name=%s WHERE form_no=%s',(phone,address,email,course,name,en))
    conn.commit()
    if y:
        x='Record Updated'
        tkMessageBox.showinfo('Demo',x)
        exit()


    else :
       x='unable to Record Updated'
       tkMessageBox.showinfo('Demo',x)
       exit()


   

def delete2(fn_entry):
    form = fn_entry.get() 
    y = cur.execute('DELETE FROM student WHERE form_no=%s' %form)
    z = cur.execute('DELETE FROM subject WHERE form_no=%s' %form)
    x = cur.execute('DELETE FROM users_stu WHERE form_no=%s' %form)
    conn.commit()
    if y:
        y = 'record deleted'
        tkMessageBox.showinfo('demo',y)
        exit()    
    else :
        exit()   


"""def delete():
    root = Tk()
    l6 = Label(root, text='enter student form no. whose record is to be deleted:',width=35)
    l6.grid(row=1,column=0)
    fn_entry = Entry(root)
    fn_entry.grid(row=1,column=1)
    delete_button = Button(root, text="delete", command= lambda:delete2(fn_entry)).grid(row=2,column=1)
    root.mainloop()"""
    
def a2(name_entry,phone_entry,email_entry):
    att = email_entry.get()
    form = name_entry.get()
    sub = phone_entry.get()
    y = cur.execute('UPDATE subject SET attendence=%s WHERE form_no=%s AND sub_name=%s',(att,form,sub))
    conn.commit()
    if y:
        y = 'attendence updated'
        tkMessageBox.showinfo('demo',y)
        exit()    
    else :
        exit()   


"""def enter_attendence():
     
    l = Label(f1abb, text='ENTER ATTENDENCE',width=40).grid(row=0)

    l1 = Label(f1abb, text='enter student form no.:',width=35).grid(row=1,column=0)
    name_entry = Entry(root)
    name_entry.grid(row=1,column=1)

    l2 = Label(f1abb, text='Enter student subject name:',width=25).grid(row=2,column=0)
    phone_entry = Entry(root)
    phone_entry.grid(row=2,column=1)


    l3 = Label(f1abb, text='enter student attendence in this subject:',width=25).grid(row=3,column=0)
    email_entry = Entry(root)
    email_entry.grid(row=3,column=1)
    att_button = Button(f1abb, text="attendence", command= lambda:a2(name_entry,phone_entry,email_entry)).grid(row=4,column=1)"""
    
    
    
def verifyla(name,password):
    
    name = name.get()
    password = password.get()
    x = cur.execute('SELECT * FROM users_fac WHERE id=%s and password=%s',(name, password))
    if x:
        y = 'permission granted!'
        tkMessageBox.showinfo('demo',y)

        root1 = Tk()
        root1.geometry("1250x650")
        root1.title("administrator")
        root1.configure(background='blue')
        Tops1=Frame(root1,width=1150,height=100,bd=16,relief="raise")
        Tops1.pack(side=TOP)
        #f = Button(root1,font=('arial',14,'bold'),text="Logout", command=exitw).pack(side=TOP)
        y = cur.execute('SELECT professor_name FROM users_fac WHERE id=%s and password=%s',(name, password))
        for y in cur:
            z = Label(Tops1,font=('arial',16,'bold'),text='welcome ').grid(row=1,column=0)
            a = Label(Tops1,font=('arial',16,'bold'),text=y).grid(row=1,column=1)
            
        f11=Frame(root1,width=250,height=500,bd=16,relief="raise")
        f11.pack(side=LEFT)
        f11.pack_propagate(0)
        f21=Frame(root1,width=750,height=500,bd=16,relief="raise")
        f21.pack(side=RIGHT)
        f21.pack_propagate(0)

        f1aaa=Frame(f11,width=250,height=500,bd=16,relief="raise")
        f1aaa.pack(side=LEFT)
        f1aaa.pack_propagate(0)

        f1abb=Frame(f21,width=750,height=500,bd=16,relief="raise")
        f1abb.pack(side=RIGHT)
        f1abb.pack_propagate(0)

        def edit_record():
           f1abb.pack_propagate(0)
         f1abb.destro(0)
           l = Label(f1abb,font=('arial',16,'bold'),text='EDIT STUDENT DETAILS').grid(row=0,column=1)

           l1 = Label(f1abb,font=('arial',14,'bold'),text='Enter student form no.: ')
           l1.grid(row=1,column=0)
           name_entry = Entry(f1abb)
           name_entry.grid(row=1,column=1)

           l2 = Label(f1abb,font=('arial',14,'bold'),text='student phone no.:')
           l2.grid(row=2,column=0)
           phone_entry = Entry(f1abb)
           phone_entry.grid(row=2,column=1)

           l3 = Label(f1abb,font=('arial',14,'bold'), text='student E-mail:')
           l3.grid(row=3,column=0)
           email_entry = Entry(f1abb)
           email_entry.grid(row=3,column=1)

           l4 = Label(f1abb,font=('arial',14,'bold'), text='student course:')
           l4.grid(row=4,column=0)
           course_entry = Entry(f1abb)
           course_entry.grid(row=4,column=1)

           l5 = Label(f1abb,font=('arial',14,'bold'), text='student name:')
           l5.grid(row=5,column=0)
           mn_entry = Entry(f1abb)
           mn_entry.grid(row=5,column=1)

           l6 = Label(f1abb,font=('arial',14,'bold'), text='student address:')
           l6.grid(row=6,column=0)
           fn_entry = Entry(f1abb)
           fn_entry.grid(row=6,column=1)

           edit_button = Button(f1abb, text="edit", command= lambda:edit_record2(name_entry,phone_entry,email_entry,course_entry,mn_entry,fn_entry)).grid(row=7,column=1)


        def input_record():
            
             l1 = Label(f1abb,font=('arial',16,'bold'),text='ENTER STUDENT DETAILS').grid(row=0,column=1)

             l1 = Label(f1abb,font=('arial',14,'bold'),text='student name: ')
             l1.grid(row=1,column=0)
             name_entry = Entry(f1abb)
             name_entry.grid(row=1,column=1)

             l2 = Label(f1abb,font=('arial',14,'bold'), text='student phone no.: ')
             l2.grid(row=2,column=0)
             phone_entry = Entry(f1abb)
             phone_entry.grid(row=2,column=1)

             l3 = Label(f1abb,font=('arial',14,'bold'), text='student E-mail: ')
             l3.grid(row=3,column=0)
             email_entry = Entry(f1abb)
             email_entry.grid(row=3,column=1)

             l4 = Label(f1abb,font=('arial',14,'bold'), text='student course: ')
             l4.grid(row=4,column=0)
             course_entry = Entry(f1abb)
             course_entry.grid(row=4,column=1)

             l5 = Label(f1abb,font=('arial',14,'bold'), text='student mother''s name: ')
             l5.grid(row=5,column=0)
             mn_entry = Entry(f1abb)
             mn_entry.grid(row=5,column=1)

             l6 = Label(f1abb,font=('arial',14,'bold'), text='student father''s name: ')
             l6.grid(row=6,column=0)
             fn_entry = Entry(f1abb)
             fn_entry.grid(row=6,column=1)

             l7 = Label(f1abb,font=('arial',14,'bold'), text='student address: ')
             l7.grid(row=7,column=0)
             address_entry = Entry(f1abb)
             address_entry.grid(row=7,column=1)

             l8 = Label(f1abb,font=('arial',14,'bold'), text='student form no.: ')
             l8.grid(row=8,column=0)
             form_no_entry = Entry(f1abb)
             form_no_entry.grid(row=8,column=1)

             l9 = Label(f1abb,font=('arial',14,'bold'), text='student enrollment no.: ')
             l9.grid(row=9,column=0)
             enrollment_no_entry = Entry(f1abb)
             enrollment_no_entry.grid(row=9,column=1)

             insert_button = Button(f1abb,font=('arial',12,'bold'),text="Insert", command= lambda: input_record2(name_entry,phone_entry,email_entry,course_entry,mn_entry,fn_entry,address_entry,form_no_entry,enrollment_no_entry)).grid(row=10)

        def delete():
           Label(f1abb,font=('arial',16,'bold'),text='DELETE RECORD').grid(row=0,column=1)
           l6 = Label(f1abb,font=('arial',14,'bold'), text='Enter student form no. whose record is to be deleted:',width=35)
           l6.grid(row=1,column=0)
           fn_entry = Entry(f1abb)
           fn_entry.grid(row=1,column=1)
           delete_button = Button(f1abb,font=('arial',12,'bold'), text="Delete", command= lambda:delete2(fn_entry)).grid(row=2,column=1)
    
        def enter_attendence():
           l = Label(f1abb,font=('arial',16,'bold'),text='ENTER ATTENDENCE').grid(row=0)
           l1 = Label(f1abb,font=('arial',14,'bold'), text='Student form no.:')
           l1.grid(row=1,column=0)
           name_entry = Entry(f1abb)
           name_entry.grid(row=1,column=1)

           l2 = Label(f1abb,font=('arial',14,'bold'),text='Subject Name:')
           l2.grid(row=2,column=0)
           phone_entry = Entry(f1abb)
           phone_entry.grid(row=2,column=1)


           l3 = Label(f1abb,font=('arial',14,'bold'),text='Enter Attendence in this subject:')
           l3.grid(row=3,column=0)
           email_entry = Entry(f1abb)
           email_entry.grid(row=3,column=1)
                      
           att_button = Button(f1abb,font=('arial',12,'bold'), text="attendence",height=2,width=20,command= lambda:a2(name_entry,phone_entry,email_entry)).grid(row=10,column=1)

        b1=Button(f1aaa,font=('arial',12,'bold'),text="attendence",height=2,width=20,command= enter_attendence).grid(row=2,column=0)
        b2=Button(f1aaa,font=('arial',12,'bold'),text=" input " ,height=2,width=20,command= input_record).grid(row=3,column=0)
        b3=Button(f1aaa,font=('arial',12,'bold'),text=" delete ",height=2,width=20,command= delete).grid(row=4,column=0)
        b4=Button(f1aaa,font=('arial',12,'bold'),text=" edit ",height=2,width=20,command= edit_record).grid(row=5,column=0)
        b5=Button(f1aaa,font=('arial',12,'bold'),text="        ",height=2,width=20,).grid(row=6,column=0)
        
        root1.mainloop()
    else:
        y = 'permission denied'
        tkMessageBox.showinfo('demo',y)
        exit()
    root.mainloop()    
       
def alogin():
    root = Tk()
    l = Label(root, text='_+_+_+_+ WELCOME TO LOGIN WINDOW, ADMINISTRATOR_+_+_+_+_').grid(row=1)
    
    l1 = Label(root, text='admin id:',width=25).grid(row=2,column=0)
    name_entry = Entry(root)
    name_entry.grid(row=2,column=1)
    
    l2 = Label(root, text='password:',width=25).grid(row=3,column=0)
    password = Entry(root,show='*')
    password.grid(row=3,column=1)

    b1 = Button(root,text="LOGIN",command= lambda: verifyla(name_entry,password)).grid(row=4,column=0)
       
    root.mainloop()    






def admin():
    l21 = Label(f1ab,font=('arial',16,'bold'),text=' WELCOME ADMINISTRATOR ')
    l21.grid(row=2,column=0)
    l11 = Label(f1ab,font=('arial',14,'bold'),text='User Name:').grid(row=3,column=0)
    name_entry = Entry(f1ab)
    name_entry.grid(row=3,column=1)
    
    l22 = Label(f1ab,font=('arial',14,'bold'),text='Password:').grid(row=4,column=0)
    password = Entry(f1ab,show='*')
    password.grid(row=4,column=1)

    b12 = Button(f1ab,font=('arial',12,'bold'),text="LOGIN",command= lambda: verifyla(name_entry,password)).grid(row=5,column=0)


    
    """l = Label(f1ab,font=('arial',16,'bold'),text=' WELCOME ADMINISTRATOR ')
    l.grid(row=6,column=1)
    l1 = Label(f1ab,font=('arial',14,'bold'),text='User Name:').grid(row=7,column=0)
    name_entry = Entry(f1ab)
    name_entry.grid(row=7,column=1)
    
    l2 = Label(f1ab,font=('arial',14,'bold'),text='Password:').grid(row=8,column=0)
    password = Entry(f1ab,show='*')
    password.grid(row=8,column=1)

    b1 = Button(f1ab,font=('arial',12,'bold'),text="LOGIN",command= lambda: verifyla(name_entry,password)).grid(row=9,column=0)
    #b = Button(f1ac,text="LOGIN",command=alogin)
    #b.pack(fill=BOTH)
    #b1=Button(f1ac,text="REGISTER",command=aregister)
    #b1.pack(fill=BOTH)"""
    


menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Login", command=alogin)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=exitw)
menubar.add_cascade(label="Administrator", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)

editmenu.add_command(label="Login", command=lstudent)

menubar.add_cascade(label="Student", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

make_button()
make_button2()



Tops.configure(background='blue')
f1.configure(background='blue')
f2.configure(background='blue')

lblInfo= Label(Tops,font=('arial',65,'bold'),text="STUDENT INFORMATION SYSTEM",bd=10)
lblInfo.grid(row=0,column=0)

root.mainloop()



    
   



