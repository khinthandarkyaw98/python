"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/26_multithreading/26_multithreading.md
Create any multithreaded code using for loop for creating multithreads
for i in range(10):
    th = Thread(target=func_name, args=(i, ))

print total active threads in multithreaded code using threading.active_count()
"""
import time
import threading

def func(num):
    for i in range(num):
        time.sleep(0.2)
        print(f"func = {i}\n")

def func2(num):
    for i in range(num):
        time.sleep(0.2)
        print(f"func2 = {i*i}\n")
        print("acive_count", threading.active_count())
        # active_count() is an inbuilt method of the threading module in Python.
        # It is used to return the number of Thread objects that are active at any instant.

a = 4

t = time.time()
t1 = threading.Thread(target=func, args=(a,))
t2 = threading.Thread(target=func2, args = (a,))

t1.start()
t2.start()

t1.join() # go back to the main program after finishing
t2.join()

print(f"The processing time = {time.time()-t}")

# The solution from the codebasics
import time
import threading
from threading import Thread

def sleepMe(i):
    print("Thread %i will sleep." % i)
    time.sleep(5)
    print("Thread %i is awake" % i)

for i in range(10):
    th = Thread(target=sleepMe, args=(i, ))
    th.start()
    print("Current Threads: %i." % threading.active_count())


