# Practical Example: 1) Write a Python program to skip 'banana' in a list using the continue statement.

List1 = ['apple', 'banana', 'mango']


for fruit in List1:
    
    if fruit == 'banana':
        continue
        
    print(fruit)