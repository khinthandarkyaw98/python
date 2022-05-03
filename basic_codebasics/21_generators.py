"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/21_generators/21_generators.md
"""
def square_seq():
    num = 1
    while True:
        yield num ** 2
        num += 1

for f in square_seq():
    if f > 100:
        break
    print(f)