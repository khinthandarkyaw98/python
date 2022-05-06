import mathlib # call the file desired to be tested

def test_cal_total(): # give prefix test_ to both filename and func_names
    total = mathlib.cal_total(3, 5)
    assert total == 8 # this means the return value should be 15

def test_cal_multiply():
    total = mathlib.cal_multiply(2, 10)
    assert total == 20

# to test
# use cmd
# go directory where the file is located
# python -m pytest
# py.test -v

