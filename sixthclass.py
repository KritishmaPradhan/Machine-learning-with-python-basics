# normal form
list1 = [2,3,4,5]
dict1 = {}
for i in list1:
    dict1[i] = i**2
print(dict1)

# dictionary comprehension
list2 = [2,3,4,5]
dist1 = {i : i**2 for i in list1}
print(dist1)

# dictionary where same above but there is no even
list2 = [2,3,4,5]
dist1 = {i : i**2 for i in list1 if i%2 != 0 }
print(dist1)

# dictionary to determine uniqueness of key
uniq_dict = {
    1 : [9,8,7],
    2 : [6,7,8],
    1 : [2,3,4]
}
print(uniq_dict)

# repersentation of dictionary for key as tuples, it cannot take list
dict2 = {
    (1,2,3) : 'attack enemy',
    (4,5,6) : 'take weapon'
}
print(dict2)
print(dict2[(1,2,3)])

# inheritance is  " is a " relationship

# inheritance  with abstract method and class
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def drive(self):
        pass
class Pagani(Vehicle):
    def drive(self):
        print("This is a car")
P = Pagani()
P.drive()
print(Pagani.__mro__)      # Method Resolution Order. It shows the order in which Python
                           #looks for methods and attributes when you call them on an object.

# inheritance example 1

class Parents:
    def __init__(self, parent_name):
        self.parent_name = parent_name
        print("the name is: ", self.parent_name)
class Child1(Parents):
    def __init__(self, parent_name, child_name):
        self.child_name = child_name
        super().__init__(parent_name)
    def display1(self):
        print(f"{self.parent_name} is the parent of {self.child_name}")
    def __str__(self):
        return f"Pname : {self.parent_name} \nCname : {self.child_name}"

C = Child1('Tina', 'Reet')
C.display1()
print(C)                       # prints the __str__ , if str not defined then it prints the location of C

# inheritance example 2 with __add__ to add two instances of class

class Point:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    def __add__(self, other):
        return self.p1 + other.p1 , self.p2 + other.p2
X = Point(2,3)
Y = Point(4,6)
print(X + Y)


