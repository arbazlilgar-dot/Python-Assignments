

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

    def __sub__(self, obj):
        m = self.a-obj.a
        n = self.b-obj.b
        return m,n

    def __mul__(self, obj):
        p = self.a * obj.a
        q = self.b * obj.b
        return p,q


obj = user(10,30)
print(obj)

obj1 = user(40,20)
print(obj1)

obj2 = user(2,3)
print(obj2)  

print("Addition : ", obj + obj1)
print("Subtraction : ", obj - obj1)
print("Multiplication : ", obj * obj1)

    
    

        
