from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val): # in Queue, enqueue is used, whereas in stack, push is used.
        self.container.appendleft(val) #in stack, append()is used
        return self.container

    def dequeue(self): #in stack, dequeue() is used.
        return self.container.pop()

    def look(self):
        return self.container

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

pq = Queue()

pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.01 AM',
    'price': 131.10
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.02 AM',
    'price': 132
})
pq.enqueue({
    'company': 'Wall Mart',
    'timestamp': '15 apr, 11.03 AM',
    'price': 135
})

print(f"pq.look = {pq.look()}")
print(f"pq.size = {pq.size()}")
print(f"pq.dequeue = {pq.dequeue()}")
print(f"pq.look = {pq.look()}")