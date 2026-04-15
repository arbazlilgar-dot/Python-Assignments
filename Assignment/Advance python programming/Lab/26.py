# Practical 16: Write a Python program to show hierarchical inheritance.


class Parent:
    def rules(self): print("Ghar ke rules sab ke liye same hai")

class Brother1(Parent):
    def work1(self): print("Brother 1 ka kaam")

class Brother2(Parent):
    def work2(self): print("Brother 2 ka kaam")

b1 = Brother1()
b2 = Brother2()
b1.rules() # dono same rule follow karenge
b2.rules()