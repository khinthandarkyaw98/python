from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, val):
        self.container.appendleft(val)
        return self.container

    def dequeue(self):
        return self.container.pop()

    def look(self):
        return self.container

    def is_empty(self):
        return len(self.container) == 0

    def size(self):
        return len(self.container)

q = Queue()
orders = ['pizza', 'samosa', 'pasta', 'biryani', 'burger']

def place_order(orders):
    for idx, order in enumerate(orders):
        print(f"{idx} = {q.enqueue(order)}")
        time.sleep(0.5)

def serve_order():
    i = 1
    try:
        while True:
            print(f"serve {i} = {q.dequeue()}")
            i += 1
            time.sleep(2)
    except Exception:
        print("Order is finished.")

if __name__ == "__main__":
    t1 = threading.Thread(target=place_order, args=(orders,))
    t2 = threading.Thread(target=serve_order)

    t1.start()
    t2.start()

    t1.join()
    t2.join()





