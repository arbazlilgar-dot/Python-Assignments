# 1. Write a Python program to import the math module and use functions like sqrt(), ceil(), floor().[cite: 1]
import math

number = 25.4

# sqrt() - square root nikalta hai
print("Square root of 25:", math.sqrt(25))

# ceil() - upar ki value deta hai
print("Ceil of 25.4:", math.ceil(number))

# floor() - niche ki value deta hai
print("Floor of 25.4:", math.floor(number))




# 2. Write a Python program to generate random numbers using the random module.[cite: 1]
import random

# 1 se 100 ke beech koi bhi random number generate karega
random_num = random.randint(1, 100)

print("Random generated number is:", random_num)