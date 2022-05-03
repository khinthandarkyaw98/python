"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/20_Iterators/20_Iterators.md
"""
class Fibonnaci:
    def __init__(self, limit):
        self.previous = 0
        self.current = 1
        self.n = 1
        self.limit = limit

    def __iter__(self): # same as for loop
        return self

    def __next__(self): # i in for loop
        if self.n < self.limit:
            result = self.previous + self.current
            self.previous = self.current
            self.current = result
            self.n += 1
            return result
        else:
            raise StopIteration

fib = Fibonnaci(10)
iter_fib = iter(fib)
while True:
    try:
        print(next(iter_fib))
    except StopIteration:
        break


