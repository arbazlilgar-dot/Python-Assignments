# Practical 18: Write a Python program to demonstrate the use of super() in inheritance.


class ParentClass:
    def msg(self):
        print("Hello main parent hu")

class ChildClass(ParentClass):
    def msg(self):
        super().msg() # parent ka function call kiya super() se
        print("Hello main child hu")

c = ChildClass()
c.msg()