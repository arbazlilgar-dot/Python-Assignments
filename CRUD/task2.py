from task1 import *

mydb = pymysql.connect(host="localhost",user="root",passwd="",database="amazon")
mycursor = mydb.cursor()

while True:
    menu = """
    press 1 for Insert Data
    press 2 for Read Data 
    press 3 for Update Data 
    press 4 for Delete Data 
    press 5 for Exit 

    """

    print(menu)
    choice = int(input("Enter Choice : "))

    if choice==1:
        name = input("Enter Name : ")
        email = input("Enter Email : ")
        password =(input("Enter Password : "))

        query = "insert into signup (name,email,password) values ('%s','%s','%s')"
        args = (name,email,password)
        mycursor.execute(query % args)
        mydb.commit()
        print("Data Inserted!!")
    

    elif choice==2:
        query = "select * from signup"

        mycursor.execute(query)

        data = mycursor.fetchall()
        print(data)

    elif choice==3:
        id = int(input("Enter Id : "))
        print("1. Name update\n2. Email update\n3. Password update")
        uch = int(input("Enter what to update : "))

        if uch == 1:
            name = input("Enter New Name : ")
            query = "update signup set name='%s' where id='%s'"
            args = (name,id)
        elif uch == 2:
            email = input("Enter New Email : ")
            query = "update signup set email='%s' where id='%s'"
            args = (email,id)
        elif uch == 3:
            password = input("Enter New Password : ")
            query = "update signup set password='%s' where id='%s'"
            args = (password,id)
        else:
            print("Galat option dala hai bhai!")
            query = None

        if query:
            mycursor.execute(query % args)
            mydb.commit()
            print("Data Updated!!")  

    elif choice==4:
        id = int(input("Enter Id : "))

        query = "delete from signup where id='%s'"
        args = (id)

        mycursor.execute(query % args)
        mydb.commit()
        print("Data Deleted!!")

    elif choice==5:
        print("Exit successfully!!")
        break