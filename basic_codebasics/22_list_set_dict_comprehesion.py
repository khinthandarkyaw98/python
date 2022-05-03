"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/22_list_set_dict_comprehension/22_list_set_dict_comprehension.md
"""

integer = [0, 1, 2, 3, 4]
binary = ["0", "1", "10", "11", "100"]

binary_dict = {key: value for key, value in zip(integer, binary)}

print(f"binary_dict = {binary_dict}")

integer = [1, -1, 2, 3, 5, 0, -7]

additive_inverse = [-inv for inv in integer]
print(f"additive_inverse = {additive_inverse}")

integer = [1, -1, 2, -2, 3, -3]

sq_set = {num**2 for num in integer}
print(f"sq_set = {sq_set}")
