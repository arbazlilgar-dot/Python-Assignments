# Practical 8: Write a Python program to handle multiple exceptions (e.g., file not found, division by zero).


try:
    f = open("ghost_file.txt", "r") # file nahi hai
    ans = 10 / 0 # zero se divide
except FileNotFoundError:
    print("Error: Bhai ye file toh exist hi nahi karti!")
except ZeroDivisionError:
    print("Error: Zero se thodi divide hota hai!")