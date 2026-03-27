# 1. Write a generator function that generates the first 10 even numbers.

def even_numbers():
    for i in range(1, 11):
        yield i * 2

for num in even_numbers():
    print(num)