import multiprocessing

def cal_sq(num, result, v, v2):
    v.value = 5.7
    v2.value = 3
    for idx, n in enumerate(num):
        result[idx] = n * n

if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    #share numbers to result while processing, i = numbers, 5 = no_of_numbers
    result = multiprocessing.Array('i', 5)

    v = multiprocessing.Value('d', 0.0)
    v2 = multiprocessing.Value('i', 0)

    p = multiprocessing.Process(target=cal_sq, args = (numbers, result, v, v2))

    p.start()
    p.join()

    print(v.value)
    print(v2.value)
    print(result[:]) # print(result) deos not work due to its multiprocessing