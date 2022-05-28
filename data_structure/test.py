# pass hello_world func as an argument to repeat func
def repeat(fn):
    fn()
    fn()

def hello_world():
    print("Hello world!")

repeat(hello_world)

"""
output
Hello world!
Hello world!
"""
print("=" * 20)
def decorator(fn):
    def hello():
        fn()
    return hello

def hello_print():
    print("Hello")

print_hello = decorator(hello_print)
print_hello()

"""
output
Hello
"""

#########################################################################################
"""
The above code can be written as follows by using @ character
"""
print("=" * 20)
def decorator_func(func):
    def wrapper():
        func()
        func()
    return wrapper

@decorator_func # this means ->>>> hello = decorator_func(hello)
def hello():
    print("Hey, Hello")

hello()