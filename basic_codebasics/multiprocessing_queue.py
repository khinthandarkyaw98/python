import multiprocessing

# child process
def cal_sq(num, q):
    for n in num:
        q.put(n * n)

# main process
if __name__ == "__main__":
    numbers = [2, 3, 5]
    que = multiprocessing.Queue()
    p = multiprocessing.Process(target=cal_sq, args=(numbers, que))

    p.start()
    p.join() # combine child with main

    while que.empty() is False:
        print(que.get())

