import numpy as np

a = np.array([[1, 2],
              [3, 5],
              [2, 9]])

print("shape : ", a.shape)

b = a.reshape(3,2)

print("b = ", b)

c = b.reshape(6, 1)
print("c", c )