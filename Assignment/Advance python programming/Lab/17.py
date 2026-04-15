# Practical 7: Write a Python program to handle exceptions in a calculator.

try:
    a = int(input("Enter pehla number: "))
    b = int(input("Enter dusra number: "))
    print("Division is:", a / b)
except Exception as error:
    # koi bhi error aayega toh yaha pakad lega
    print("Oops, kuch gadbad ho gayi:", error)