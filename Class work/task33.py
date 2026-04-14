from abc import ABC, abstractmethod

class vehicle(ABC):
    @abstractmethod
    def tyres(self):
        pass


    def color (self):
        pass

class bike(vehicle):
    def tyres(self):
        return " Two Wheeler"
    
    def color(self):
        return " BLACK COLOUR "
    
class car(vehicle):
    def tyres(self):
        return " Four Wheeler"
    

    def color(self):
        return " WHITE COLOUR "
    
class auto(vehicle):
    def tyres(self):
        return " Three Wheeler"
    

    def color(self):
        return " YELLOW AND GREEN COLOUR"
    

v1= bike()
print(v1.tyres())
print(v1.color())


v2 = car()
print(v2.tyres())
print(v2.color())

v3 = auto()
print(v3.tyres())
print(v3.color())