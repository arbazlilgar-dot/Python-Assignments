# Q.10 Write Python programs to demonstrate method overloading and method overriding.

# 1. Overloading (Python me direct nahi hoti, default value se karte hai)
class MathCalc:
    def add(self, a, b, c=0):
        return a + b + c

m = MathCalc()
print("Overloading (2 args):", m.add(10, 20))
print("Overloading (3 args):", m.add(10, 20, 30))

# 2. Overriding   
class Parent:
    def my_func(self):
        print("Parent wala function")

class Child(Parent):
    def my_func(self): # same naam ka function child me
        print("Child wala function (Overridden)")

c = Child()
c.my_func() # child wala hi chalega