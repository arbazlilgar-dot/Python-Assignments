# 1. Write a Python program to create a function that takes a string as input and prints it.[cite: 1]
def print_message(text):
    print("Mera message hai:", text)

# Function ko call kar rahe hain
print_message("Assignment khatam hone wala hai!")




# 2. Write a Python program to create a calculator using functions.[cite: 1]
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

num1 = 20
num2 = 10

print("Addition:", add(num1, num2))
print("Subtraction:", subtract(num1, num2))