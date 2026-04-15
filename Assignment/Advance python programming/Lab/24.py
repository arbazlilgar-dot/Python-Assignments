# Practical 14: Write a Python program to show multilevel inheritance.


class GrandFather:
    def land(self): print("Grandfather")

class Father(GrandFather):
    def house(self): print("dad house ")

class Child(Father):
    def car(self): print("child bike")

c = Child()
c.land()
c.house()
c.car()