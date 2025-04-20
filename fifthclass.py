# OOP Concept class and object
class Vehicle:
    def __init__(self, wheels, seats, enigne_type, breaks, name):
        self.wheels = wheels                                       # self is actually an object (V = self)
        self.seats = seats
        self.engine_type = enigne_type
        self.breaks = breaks
        self.name = name
    def drive(self):
        print("printing attributes:  ", self.wheels, self.seats,self.engine_type, self.breaks, self.name)
V = Vehicle(2, 4,'good', 'works' , 'Thar')
V.drive()

class Person:
    pass
P1 = Person()
P1.name = "Kriti"
print(P1.name)
print(P1)

# data encapsulation with private class variables
class Printing:
    def __init__(self, name):
        self.__name = name
    def briefing(self):
        print(self.__name)
P = Printing('Kritishma')
P.briefing()
# P.__name = 'Pradhan'                                          # name mangling (can be modified even when private)   
# print("This throws error as it is private __name", P.__name)
P.briefing()
print(P._Printing__name)                                        # now we can access it outside the class though it is private
