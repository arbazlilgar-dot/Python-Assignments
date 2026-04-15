# Q.6 Write a Python program to handle exceptions in a simple calculator (division by zero, invalid input).

try:
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    ans = n1 / n2
    print("Answer is:", ans)
except ZeroDivisionError:
    print("Error: 0 se divide mat kar bhai")
except ValueError:
    print("Error: Sahi number daal, text nahi")