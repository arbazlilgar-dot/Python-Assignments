from abc import ABC,abstractmethod

class Employer(ABC):
    @abstractmethod
    def salary(self):
        pass


class Raj(Employer):
    def salary(self):
        return 10000
    

class Arbaz(Employer):
    def salary(self):
        return 20000
    

obj = Raj()
print(obj.salary())

obj1 = Arbaz()
print(obj1.salary())