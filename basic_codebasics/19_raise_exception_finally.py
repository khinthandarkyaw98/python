"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/19_raise_exception_finally/19_raise_exception_finally.md
"""
# exercise 1
class AdultException(Exception):
   pass

a = AdultException()

# exercise 2
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# exercise 3
    def get_minior_age(self):
            if int(self.age) >= 18:
                raise AdultException
            else:
                return self.age

# exercise 4
    def display_person(self):
        try:
            print(f"age -> {self.get_minior_age()}")
        except AdultException:
            print("This person is an adult")
        finally:
            print(f"name -> {self.name}")

Person("Nick", 17).display_person()
Person("Joe", 20).display_person()
