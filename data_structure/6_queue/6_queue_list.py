wmt_stock_price_queue = []

# Queue is FIFO, whereas stack is LIFO.

# we always insert the queue at zero position.
wmt_stock_price_queue.insert(0, 131.10)
wmt_stock_price_queue.insert(0, 132.12)
wmt_stock_price_queue.insert(0, 135)

print(f"wmt_stock_price_queue = {wmt_stock_price_queue}")

print(f"wmt_stock_price_queue.pop() = {wmt_stock_price_queue.pop()}")

"""
output
wmt_stock_price_queue = [135, 132.12, 131.1]
wmt_stock_price_queue.pop() = 131.1
"""