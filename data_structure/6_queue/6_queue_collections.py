from collections import deque

q = deque()

q.appendleft(5) # in stack, appendleft() is used.
q.appendleft(6)
q.appendleft(7)

print(f"q = {q}")

print(f"q.pop() = {q.pop()}")

"""
output
q = deque([7, 6, 5])
q.pop() = 5
"""

