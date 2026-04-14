import random
ac_no = random.randint(1001,9999)
class bank:
    def ac_register(self):
        name = input("Enter Name : ")
        email= input("Enter Email : ")
        self.pin=input("Enter pin : ")
        bal = 25000
        print("Genrated account number is :",ac_no)
        print("Your initial balance : ",bal)
        self.bal=bal

    def deposite(self):
        p = input("enter pin:")
        if p==self.pin:
            damount = int(input("Enter Deposit Amount : "))
            self.bal+=damount

            print("Deposite Successfully!!")
        else:print("wrong pin!!!")

    def Withdraw(self):
        p = input("enter pin :")
        if p==self.pin:
            wamount = int(input("Enter Witdrawl Amount :"))
            if self.bal>wamount:
                self.bal-=wamount
                print("Withdraw Successfully!!")
            else:print("Insufficient Balance!!!")
        else:print("wrong pin!!!")

    def checkbal(self):
        p = input("enter pin: ")
        if p==self.pin:
            print("Ypur Balance is : ",self.bal)
        else:print("wrong pin!!!")

obj = bank()
while True:
    menu = """"
        Press 1 for Register
        Press 2 for Exit
    """ 

    print(menu)
    choice = int(input("Enter Choice :"))

    if choice==1:
        obj.ac_register()
        while True:
         menu1= """
         Press 1 for Deposit
         Presss 2 for Withdrawl
         Press 3 for Check Balance
         Press 4 for Exit 

         """

         print(menu1)
         choice1= int(input("Enter Choice :"))
         if choice1 ==1:
             obj.deposite()
         
         elif choice1 == 2:
             obj.Withdraw()
         
         elif choice1 == 3:
             obj.checkbal()
         
         elif choice1 == 4:
             break
          
         else:
             print("Invalid Choice!!!")

    elif choice==2:
        break

    else:
        print("Invalid Number ")