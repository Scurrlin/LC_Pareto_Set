# Queues
# ======
# A queue is a linear data structure that follows a particular order in which
# the operations are performed. The order is FIFO (First In First Out).

from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3)
print(queue.popleft())  # Output: 1
print(queue)  # Output: deque([2, 3])