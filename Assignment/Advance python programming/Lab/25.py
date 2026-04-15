# Practical 15: Write a Python program to show multiple inheritance.


class Partner1:
    def invest_1(self): print("Rehan's Investment")

class Partner2:
    def invest_2(self): print("Sadik's Investment")

class Business(Partner1, Partner2): # Dono partner se inherit kiya
    def profit(self): print("Total Business Profit")

b = Business()
b.invest_1()
b.invest_2()