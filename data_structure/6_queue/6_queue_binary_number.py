from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)
        return self.container

    def dequeue(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

def front():
    q.enqueue("1") # 1
    for i in range(10):
        peek = q.peek() # 1
        print(peek) # 1
        q.enqueue(peek + "0") # deque[10, 1]
        q.enqueue(peek + "1") # deque[11, 10, 1]
        q.dequeue() # pop 1, deque[ 11, 10]

if __name__ == "__main__":
    q = Queue()
    front()

"""
i == 1 :
    peek -> 1
    deque[10, 1]
    deque[11, 10, 1]
    pop 1, deque[11, 10]
i == 2 :
    peek -> 10
    deque [100, 11, 10]
    deque [101, 100, 11, 10]
    pop 10, deque [101, 100, 11]
i == 3 :
    peek -> 11
    deque [110, 101, 100, 11]
    deque [111, 110, 101, 100, 11]
    pop 11, deque[111, 110, 101, 100]
    .
    .
    .
    .
"""





