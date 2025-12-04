"""
Producer Thread
Reads product data from a source list and inserts items into the BlockingQueue.
"""

import threading


class Producer(threading.Thread):
    """
    Producer thread that pushes items into the shared blocking queue.
    """

    def __init__(self, source, queue):
        """
        :param source: List of Product objects to be produced.
        :param queue: The BlockingQueue instance for data transfer.
        """
        super().__init__(name="ProducerThread")
        self.source = source
        self.queue = queue

    def run(self):
        """
        Continuously inserts items into the queue until all items are produced.
        """
        for product in self.source:
            print(f"[Producer] Producing: {product}")
            self.queue.put(product)
        print("[Producer] Finished producing all items.")
