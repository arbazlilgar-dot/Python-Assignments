# Q.9 Write Python programs to demonstrate different types of inheritance (single, multiple, multilevel, etc.).


class GrandParent:
    def show_g(self):
        print("GrandParent class")

class Parent(GrandParent):
    def show_p(self):
        print("Parent class")

class Child(Parent):
    def show_c(self):
        print("Child class")

c = Child()
c.show_c() # khud ka
c.show_p() # parent ka
c.show_g() # grandparent ka