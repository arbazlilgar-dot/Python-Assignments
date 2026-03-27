# 2. Write a Python program that uses reduce() to find the product of a list of numbers.


from functools import reduce

def multiply(a, b):
    return a * b

numbers = [1, 2, 3, 4]
result = reduce(multiply, numbers)
print(result)