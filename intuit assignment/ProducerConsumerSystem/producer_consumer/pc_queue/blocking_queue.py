"""
BlockingQueue Module
Implements a thread-safe blocking queue using Locks and Condition variables.
"""

import threading
from collections import deque


class BlockingQueue:
    """
    A custom thread-safe blocking queue with fixed capacity.
    This queue blocks the producer when it is full and blocks the consumer
    when it is empty. Synchronization is handled via Condition variables.
    """

    def __init__(self, capacity: int):

        """
        Initialize the queue with a fixed capacity.
        
        :param capacity: Maximum number of items allowed in the queue.
        :raises ValueError: If capacity is zero or negative.
        """
        if capacity <= 0:
            raise ValueError("BlockingQueue capacity must be greater than zero.")
        
        self.capacity = capacity
        self.queue = deque()
        self.lock = threading.Lock()  # Mutual exclusion lock
        self.not_empty = threading.Condition(self.lock)  # For consumer wait/notify
        self.not_full = threading.Condition(self.lock)   # For producer wait/notify

    def put(self, item):
        """
        Insert an item into the queue.
        If the queue is full, the producer thread waits.

        param item: The item to insert into the queue.
        """
        with self.not_full:
            while len(self.queue) >= self.capacity:
                self.not_full.wait()

            self.queue.append(item)

            # Notify one consumer thread that queue is not empty anymore
            self.not_empty.notify()

    def take(self):
        """
        Remove and return an item from the queue.
        If the queue is empty, the consumer thread waits.

        :return: The removed item.
        """
        with self.not_empty:
            while not self.queue:
                self.not_empty.wait()

            item = self.queue.popleft()

            # Notify one producer that queue has space
            self.not_full.notify()
            return item
