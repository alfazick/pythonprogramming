from mypackage import code
from mypackage import animal

from mypackage.animal import Animal


p = code.Person("John")
p.say_hello()

a = animal.Animal("auf")
a.say()

b = Animal("muy")
b.say()

# main.py
# mypackage/
    # code.py 
    # animal.py