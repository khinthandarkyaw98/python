"""
this divides the work into different CPU cores
to reduce the duration of the processing
watch it : https://www.youtube.com/watch?v=_1ZwkCY9wxk&list=PLeo1K3hjS3uv5U-Lmlnucd7gqF-3ehIh0&index=34
"""

from multiprocessing import Pool
import time

def f(n):
    return n * n

if __name__ == "__main__":
    t1 = time.time()
    p = Pool(processes = 3) # divide 3 process
    result = p.map(f, range(1,10000))
    for n in result:
        a = n
    print(f"processing time with pool func: {time.time()-t1}")

