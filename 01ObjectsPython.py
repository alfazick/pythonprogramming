# Type Hints

print(type("Hello, world"))
print(type(42))

name = "Hello"
print(id(name)) # id of an object it refers to

# Type hints checking

def odd(n: int) -> bool:
    return n % 2 != 0

# Creating a class

class MyFirstClass:
    pass 

a = MyFirstClass()
print(a)

# Adding attributes on a fly
class Point:
    pass

p1 = Point()
p1.x = 5
p1.y = 4

print(p1.x)

class Point:
    def reset(self):
        self.x = 0
        self.y = 0

p = Point()
p.reset() # or Point.reset(p)

print(p.x,p.y)

# More arguments
import math 
class Point:
    def move(self, x: float,y: float) -> None:
        self.x = x
        self.y = y 

    def reset(self) -> None:
        self.move(0,0)

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)
    

point1 = Point()
point2 = Point()
point1.reset()
point2.move(5,0)
print(point2.calculate_distance(point1)) 

# The assert statement
# program will fail if the expression after assert evaluates to False (or zero, empty, or None)
assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

point1.move(3,4)

print(point1.calculate_distance(point2))
print(point2.calculate_distance(point1))

# Create constructors

class Point:
    def __init__(self, x: float, y: float) -> None:
        self.move(x,y)

    def move(self,x:float,y:float) -> None:
        self.x = x
        self.y = y 

    def reset(self) -> None:
        self.move(0,0)

    def calculate_distance(self, other: "Point") -> float:
        return math.hypot(self.x - other.x, self.y - other.y)


point = Point(3,5)
print(point.x, point.y)

# Default arguments 

# class Point:
#     def __init__(
#             self,
#             x: float = 0,
#             y: float = 0
#     ) -> None:
#         self.move(x,y)
        
# Modules and Packages

# model.py is a module named model inside of local directory
 
# from database import Database,Query 

# Organizing Modules
