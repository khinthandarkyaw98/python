import numpy as np

a = np.array([  [1, 3],
                [3, 1],
                [3, 4]
                ])

b = np.array([  [1, 2],
                [2, 2],
                [6, 2]
                ])

# axis 0  = column
# axis 1 = row

print(f"maximum = {a.max()}")
print(f"minimum = {a.min()}")
print(f"sum = {a.sum()}\n")
print(f"sum(axis=0) = {a.sum(axis=0)}")
print(f"sum(axis=1) = {a.sum(axis=1)}\n")

# sqrt() is a generic function.
# np.sqrt(array) can only be available.

print(f"square_root =\n"
      f"{np.sqrt(a)}\n")

# standard_deviation
print(f"standard_deviation =\n"
      f"{np.std(a)}\n")

# addition
print(f"addition =\n"
      f"{a+b}")

# subtraction
print(f"subtraction =\n"
      f"{a-b}")

# multiplication
print(f"multiplication =\n"
      f"{a*b}")

# dot product
# a.shpae = (3, 2), b.shape = (3,2)
# therefore dot product is inavailable, b.transpose is performed to get (2, 3)
c = np.transpose(b)
print(f"dot product =\n"
      f"{a.dot(c)}")
