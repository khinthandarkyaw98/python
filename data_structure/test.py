def binary_func(a):
    for i in range(1, a+1): # 1
        if i == 1:
            print(1)
        else:
            j = i
            rem_total = 0
            count = 1
            while j != 0:
                rem = j % 2
                rem_total = rem_total + count * rem
                count *= 10
                j = j // 2
            ans = rem_total
            print(ans)

if __name__ == "__main__":
    binary_func(int(input("Enter a number")))
    
"""
Enter a number4
1
10
11
100
"""

"""
debug
i = 1: return 1
i = 2: j= 2, rem_total = 0, count = 1, rem = 0, rem_total = 0, count = 10, j = 1
       j= 1, rem_total = 0, count = 10, rem = 1, rem_total  = 10, count = 100, j = 0, ans = 10
i = 3: j = 3, rem_total = 0, count = 1, rem = 1, rem_total = 1, count = 10, j = 1
       j = 1, rem_total = 1, count = 10, rem = 1, rem_total = 11, count = 100, j = 0, ans = 11
i = 4, j = 4, rem_total = 0, count = 1, rem = 0, rem_total = 0, count = 10, j = 2
       j = 2, rem_total = 0, count = 10, rem = 0, rem_total = 0, count = 100, j = 1
       j = 1, rem_total = 0, count = 100, rem = 1, rem_total = 100, count = 1000, j = 0, ans = 100
"""






