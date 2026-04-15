# Practical 19: Write a Python program to show method overloading.



class Calculator:
    def add(self, a, b, c=0): # c ko default 0 rakha hai
        return a + b + c

calc = Calculator()
print("2 numbers ka total:", calc.add(10, 20))
print("3 numbers ka total:", calc.add(10, 20, 30))