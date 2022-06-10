from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def push(self, val):
        self.container.append(val)
        return self.container

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def look(self):
        return self.container

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def reverse_string(s):
    stack = Stack()

    for ch in s:
        stack.push(ch)

    rstr = ''
    while stack.size()!=0:
        rstr += stack.pop()

    return rstr


if __name__ == '__main__':
    print(reverse_string("We will conqure COvID-19"))
    print(reverse_string("I am the king"))
    
    a = Stack()

    print("Push 5, 6, 7 into deque:")
    print(a.push(5))
    print(a.push(6))
    print(a.push(7))

    print(f"a.pop() = {a.pop()}")

    print(f"a = {a.look()}")

    print(f"size of a = {a.size()}")

    print(f"Is the deque empty? : {a.is_empty()}")

    print(f"a.peek() = {a.peek()}")

"""
output 

91-DIvOC eruqnoc lliw eW
gnik eht ma I
Push 5, 6, 7 into deque:
deque([5])
deque([5, 6])
deque([5, 6, 7])
a.pop() = 7
a = deque([5, 6])
size of a = 2
Is the deque empty? : False
a.peek() = 6

"""