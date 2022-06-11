def binary_func(a):
    for i in range(1, a+1): # 1
        if i == 1:
            print(1)
        else:
            j = i
            rem_total = 0
            count = 1
            while j != 0:
                div = j // 2
                rem = j % 2
                rem_total = rem_total + count * rem
                count *= 10
                j = j // 2
            ans = rem_total
            print(ans)

if __name__ == "__main__":
    binary_func(int(input("Enter a number")))






