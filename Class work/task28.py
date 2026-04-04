class MYclass :
    def reverse_value(self):
        value =input("Enter value for reverse : ")
        print("Reverse value :",value[::-1])

        
    def find_duplicates(self):
        data = input("Enter number for find duplicates :")
        unique = []
        duplicates = []

        for item in data:
            if item not in unique:
                unique.append(item)
            elif item not in duplicates:
                duplicates.append(item)
        
        print("Duplicates Values : ",duplicates)

    def check_palindrome(self):
        value = input("Enter a string of number :")
        if value == value[::-1]:
            print("IT is a palindrome")
        else:
            print("It is not a palindrome")

obj = MYclass()
while True:
    menu = """"
    press 1 for Reverse
    press 2 for Duplicate Find
    press 3 for Palindrome
    press 4 for Exit
    
    """
    print(menu)
    choice = int(input("Enter the Choice : "))

    if choice == 1:
        obj.reverse_value()

    if choice == 2:
        obj.find_duplicates()

    if choice == 3:
        obj.find_duplicates()

    if choice == 4:
        break
    