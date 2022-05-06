"""
in shared data while processing,
the result can be inconsistent
to prevent this, lock has to be used
"""
import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value += 1
        lock.release()


def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        balance.value -= 1
        lock.release()


if __name__ == "__main__":
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args =(balance, lock))
    w = multiprocessing.Process(target=withdraw, args = (balance, lock))

    d.start()
    w.start()

    d.join()
    w.join()

    print(balance.value) # print(balance) does not work due to its shared data processing nature


