# 3. Write a Python program that filters out even numbers using the filter() function.


def check_even(n):
    if n % 2 == 0:
        return True
    return False

numbers = [1, 2, 3, 4, 5, 6]
result = list(filter(check_even, numbers))
print(result)