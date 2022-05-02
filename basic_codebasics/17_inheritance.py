"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/17_inheritance/17_inheritance.md
"""
class Anmial:
    def __init__(self, habitat):
        self.habitat = habitat

    def print_type(self):
        print(self.habitat)

    def sound(self):
        print("The Sound of this animal is")

class Dog(Anmial):
    def __init__(self):
        super().__init__("Dog")

    def soung(self):
        Anmial.sound(self) # we need to pass (self) if we use classname
        super().sound() # we do not need to pass self if we use super()
        print("Woof WOOF")

d = Dog()
d.print_type()
d.soung()