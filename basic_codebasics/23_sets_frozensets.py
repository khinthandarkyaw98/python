"""
https://github.com/codebasics/py/blob/master/Basics/Exercise/23_sets_frozensets/23_sets_frozensets.md
"""
a = set()
a.add(1)
a.add(2)
a.add(1)
print(f"set = {a}")
b = frozenset(a)
print(f"frozenset = {b}")

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

#diffrence between set1 and set2 is {1, 2, 3}
print("By using minus operator")
print(f"difference between set1 and set2 is {set1-set2}\n")
print("By using 'differnce' buit-in method")
print(f"difference between set1.diffence(set2) is {set1.difference(set2)}")
print(f"difference between set2.diffence(set1) is {set2.difference(set1)}")
