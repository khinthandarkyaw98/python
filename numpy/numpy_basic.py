import numpy as np
import time

# create numpy array
a1 = np.array([1, 2, 3])
a2 = np.array([1, 3, 5])

print(f"numpy array addition: {a1 + a2}")

size = 10000000

# create the normal list
l1 = range(size)
l2 = range(size)

# create the numpy array
n1 = np.arange(size)
n2 = np.arange(size)

# python list
start1 = time.time()
r1 = [(x+y) for x, y in zip(l1, l2)] # list comprehension
print(f"python list took: {time.time()-start1}s.")

# numpy operation
start2 = time.time()
r2 = n1 + n2 # no need to comprehend, direct operation is available
print(f"numpy list took: {time.time()-start2}s.")

