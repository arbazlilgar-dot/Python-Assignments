

class user():

    def __init__(self,a,b):       #Constructor by default
        self.a=a
        self.b=b    


    def __str__(self):
        return f"{self.a}, {self.b}"



    def __add__(self, obj):
        x = self.a+obj.a
        y = self.b+obj.b                                            

        return x,y         


obj = user(10,30)
print(obj)

obj1 = user(40,20)
print(obj1)


print("Additional : ",obj+obj1)         


    
    

        







