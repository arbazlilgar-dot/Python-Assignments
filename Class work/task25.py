def check_palindrom():
    value = input("Enter a string or number :")
    if value == value[::-1]:
        print("It is a Palindrome")
    else:
        print("It is not a palindrome")

def ascending_descending():
    data = input("Enter numbers seprated by space :").split()

    try:
        numbers =[int(x) for x in data]
    except ValueError:
        print("Please enter valid integers.")
        return
    
    print("1. Ascending")
    print("2.Descending")

    choice =input("Enter sort type:")

    if choice == '1':
        numbers.sort()
        print("Ascending order :",numbers)
    elif choice =='2':
        numbers.sort(reverse=True)
        print("Descending order :",numbers)
    else:
        print("Invalid sort choice")

def reverse_value():
    value = input("Enter value to reverse:")
    print("Reversed value",value[::-1])

def find_duplicates():
    data = input("Enter element seprated by space:").split()
    unique = []
    duplicates = []

    for item in data:
        if item not in unique:
            unique.append(item)
        elif item not in duplicates:
            duplicates.append(item)

    print("Duplicate values :",duplicates)

while True:
    menu = """
    press 1 for Palindrome
    press 2 for Ascending/Descending
    press 3 for Reverse
    press 4 for Duplicate
    press 5 Exit

"""
    print(menu)
    choice = int(input("Enter Choice"))

    if choice == 1:
     check_palindrom()

    elif choice == 2:
     ascending_descending()

    elif choice == 3 :
     reverse_value()

    elif choice == 4:
     find_duplicates()

    elif choice == 5:
        print("Exiting..")
        break
    else:
       print("Invalid Choice!!!")




