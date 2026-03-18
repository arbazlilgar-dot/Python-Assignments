def even_odd():
    n=int(input("Enter Number : "))

    if n%2==0:
        print("Even !!")

    else:
        print("odd !")

def check_prime():
    num = int(input("Enter a number to check Prime: "))
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("Not a Prime Number")
                break
        else:
            print("Prime Number")
    else:
        print("Not a Prime Number")

def factorial():
    num = int(input("Enter a number for Factorial: "))
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    print("Factorial is:", fact)

while True:

    menu = """
    press 1 for check even_odd Number
    press 2 for Check Prime number
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
        print("Thank you !!")
        break
    else:
        print("Invalid choice !")

   