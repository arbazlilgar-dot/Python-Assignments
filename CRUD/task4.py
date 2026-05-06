from tkinter import * 


def login():

    root = Tk()

    root.geometry("500x500")
    root.title("Login!!")


    email = Label(root,text="Email",font=("Arial,16,bold"))
    email.place(x=50,y=50)

    root.mainloop()