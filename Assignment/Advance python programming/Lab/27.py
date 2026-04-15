# Practical 17: Write a Python program to show hybrid inheritance.


# combination of different inheritances
class A:
    def displayA(self): print("Class A")
class B(A):
    def displayB(self): print("Class B")
class C(A):
    def displayC(self): print("Class C")
class D(B, C):
    def displayD(self): print("Class D (Hybrid)")

d_obj = D()
d_obj.displayA()
d_obj.displayD()