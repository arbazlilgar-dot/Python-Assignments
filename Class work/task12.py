#menu driven 

while True:

    menu = """
    press 1 for Right angle pattern
    press 2 for Factorial
    press 3 for Prime number
    press 4 for Exit 

"""
    print(menu)

    choice = int (input("Enter Choice :"))

    if choice ==1:
        for i in range(1,6):
            print("*"*i)
    
    elif choice==2:

        num = int(input("Enter a number: "))
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        print("Factorial is:", fact)

    elif choice==3:
         num = int(input("Enter a number: "))
         if num > 1:
             for i in range(2, num):
                 if (num % i) == 0:
                     print("Not a Prime Number")
                     break
             else:
                 print("Prime Number")
         else:
             print("Not a Prime Number")

       
    elif choice==4:
        print("Thank you !!")
        break
    else:
        print("Invalid choice !")
        break
