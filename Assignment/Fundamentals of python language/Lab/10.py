# Practical Example 6: Write a Python program to check if a number is prime using if_else.

num = 7
prime = True

# checking prime condition by dividing number
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            prime = False
            break
            
    if prime:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print(num, "is not a prime number")