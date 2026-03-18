import random

original = random.randint(1,51)

print("************ Enter Number Between 1 to 50!! ******************")

while True:
    Choice = int(input("Enter Number Between 1 to 50!"))

    if Choice>50:
        print("INVALID NUMBER!!")

    elif original == Choice:
        print("WIN")

    elif Choice>original:
        print("Original number is less than entered number!!")

    else:
        print("Original number is greater than enterd number!!")
        