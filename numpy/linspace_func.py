# linspace() means the divide the interval between the start and the end equally according the step

# linspace(start, end, step)

import numpy as np

a = np.linspace(1, 3, 10)
print("a = ", a)
"""
output : 
a =  [1.         1.22222222 1.44444444 1.66666667 1.88888889 
                            2.11111111, 2.33333333 2.55555556 2.77777778 3.        ]
"""

b = np.linspace(1, 2, 20)
print("b = ", b)
""""
output:
b =  [1.         1.05263158 1.10526316 1.15789474 1.21052632 1.26315789
 1.31578947 1.36842105 1.42105263 1.47368421 1.52631579 1.57894737
 1.63157895 1.68421053 1.73684211 1.78947368 1.84210526 1.89473684
 1.94736842 2.        ]
"""