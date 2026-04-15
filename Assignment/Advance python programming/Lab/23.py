# Practical 13: Write a Python program to show single inheritance.


class Father:
    def home(self):
        print("Father ka ghar")

class Son(Father): # Son ne Father se inherit kiya
    def bike(self):
        print("Son ki bike")

s = Son()
s.home() # Father ka function access kar liya
s.bike()