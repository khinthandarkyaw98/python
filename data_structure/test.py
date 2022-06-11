# this file is just for testing only.
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

print("*" * 20)

########################################################################################
def repeat_decorator(num_repeat = 2): # num_repeat = 5
    def inner_decorator(fn):
        def decorated_fn():
            for i in range(num_repeat):
                fn()
        return  decorated_fn
    return inner_decorator

@repeat_decorator(5) # hello_world = repeat_decorator(hello_world)
def hello_world():
    print("Hello World!")

hello_world()

"""
import time
def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__ + " took " 
        + str((end-start)*1000) + "mil sec")
        return result
    return wrapper
    
    
# this file is saved as util.py

# we can call the file as follows in another .py file

from util import time_it
@time_it # before the func we want to measure the time
"""
match = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }

print(match["}"] == "{")
