# using deque as a stack
from collections import deque
stack = deque()

stack.append("1")
print(f"stack = {stack}")

stack.append("2")
print(f"stack = {stack}")

stack.pop()
print(f"stack after pop() = {stack}")

"""
output
stack = deque(['1'])
stack = deque(['1', '2'])
stack after pop() = deque(['1'])
"""