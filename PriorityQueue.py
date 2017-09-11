import heapq
from time import time

class PriorityQueue:
    def __init__(self):
		"""Initialize an empty priority queue."""
		
        self._queue = []
        self._index = 0

    def __len__(self):
		"""The number of entries in the queue."""
		
        return len(self._queue)

    def push(self, item, priority):
		"""Add an item to the priority queue with the specified priority."""
		
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def pop(self):
		"""Return the smallest priority value and remove it from the queue."""
		
        return heapq.heappop(self._queue)[-1]
