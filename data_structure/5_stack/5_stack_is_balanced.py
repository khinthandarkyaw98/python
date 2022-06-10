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

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def is_match(ch1, ch2): # is_match("}", "{")
    match = {
        "}" : "{",
        ")" : "(",
        "]" : "["
    }
    return match[ch1] == ch2 # "{" == "{"

def is_balanced(s):
    stack = Stack()
    for ch in s:
        if ch == "{" or ch == "(" or ch == "[":
            stack.push(ch) # stack.pop()-> "{"
        if ch == "}" or ch == ")" or ch == "]":
            if stack.size() == 0:
                return False
            if not is_match(ch, stack.pop()): # is_match("}", "{")
                return False
    return stack.size() == 0

if __name__ == "__main__":
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))


