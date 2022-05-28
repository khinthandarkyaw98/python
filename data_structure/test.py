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

