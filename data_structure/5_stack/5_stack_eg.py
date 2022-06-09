# using a list as a stack
s = []
s.append("a")
s.append("b")
s.append("c")

print(f"s = {s}")
print(f"s.pop() = {s.pop()}")
print(f"s after pop() = {s}")
print(f"s[-1] = {s[-1]}")
print(f"s after s[-1] = {s}")

"""
output 
s = ['a', 'b', 'c']
s.pop() = c
s after pop() = ['a', 'b']
s[-1] = b
s after s[-1] = ['a', 'b']
"""

