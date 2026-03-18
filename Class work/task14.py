def even_odd():
    n= int (input("Enter Number :"))

    if n%2==0:
        print(" Even !!")
    else:
        print(" Odd !")

def check_prime():
    num=int (input("Enter a number to check prime :"))
    if num>1:
        for i in range(2,num):
            if (num % i) ==0:
                print("Not a prime Number ")
                break
        else:
            print("Prime Number")
    else:
        print("Not a prime number")

def factorial():
    num= int(input("Enter a Number for Factorial :"))
    fact = 1
    for i in range(1, num +1):
        fact=fact *i
    print("Factorial is :", fact)

while True:

    menu = """

    press 1 for Check even_odd Number
    press 2 for Check Prime Number
    press 3 for Factorial
    press 4 for Exit    
     
    """
    print(menu)

    choice = int (input("Enter Choice :"))
    if choice == 1:
        even_odd()
    elif choice == 2:
        check_prime()
    elif choice == 3:
        factorial()
    elif choice == 4:
        print("Thank You !!")
        break
    else:
        print(" Invaid Choice !!") 
