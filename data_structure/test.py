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

