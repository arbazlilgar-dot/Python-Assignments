from tkinter import * 
from task4 import *
root = Tk()

root.geometry("500x500")

root.title("Registration!!")

name = Label(root,text="Enter Name",font=("Arial",12,"bold"))
name.place(x=50,y=50) 

email = Label(root,text="Enter Email",font=("Arial",12,"bold"))
email.place(x=50,y=100)

mobile = Label(root,text="Enter Mobile",font=("Arial",12,"bold"))
mobile.place(x=50,y=150)

password = Label(root,text="Enter password",font=("Arial",12,"bold"))
password.place(x=50,y=200)

cpassword = Label(root,text="Enter Conform Password",font=("Arial",12,"bold"))
cpassword.place(x=50,y=250)


ename = Entry(root,bg="Yellow")
ename.place(x=250,y=60)

eemail = Entry(root,bg="Yellow")
eemail.place(x=250,y=110)

emobile = Entry(root,bg="Yellow")
emobile.place(x=250,y=160)

epassword = Entry(root,bg="Yellow")
epassword.place(x=250,y=210)

ecpassword = Entry(root,bg="Yellow")
ecpassword.place(x=250,y=260)


insert = Button(root,text="Insert",font=("Arial",16,"italic"),fg="red",command=login)
insert.place(x=50,y=330)

search = Button(root,text="Search",font=("Arial",16,"italic"),fg="red")
search.place(x=150,y=330)

update = Button(root,text="Update",font=("Arial",16,"italic"),fg="red")
update.place(x=270,y=330)

delete = Button(root,text="Delete",font=("Arial",16,"italic"),fg="red")
delete.place(x=390,y=330)

root.mainloop()  


