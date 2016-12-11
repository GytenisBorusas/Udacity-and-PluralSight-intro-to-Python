'''
    File name: oopconcepts.py
    Author: Gytenis Borusas
    Date created: 12/10/2016
    Date last modified: 12/10/2016
    Python Version: 3.5

    OOP concepts.
'''

class Person:       # Here we define class called "Person"

    def __init__(self, name):       # Here we initialize input to be
        # the "name".
        self.name = name

    def say_hello(self):
        print(id(self))     # we show the memory allocation for the
        # first input.
        print("Hello!", self.name)

p1 = Person("Scott")    # we define what is our input "name".
p2 = p1     # We point our p2 variable to the same address as the
# variabe p1.
p2.name = "Alex"        # We define variable p2, which is not
# associated with the same memory place as the variable p1 and thats
# why they boths are the same at the moment.
print(id(p1))
print(id(p2))
p1.say_hello()
