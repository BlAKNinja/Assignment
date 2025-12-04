"""
Consumer Thread
Fetches Product items from the BlockingQueue and stores them in destination list.
"""

import threading


class Consumer(threading.Thread):
    """
    Consumer thread that retrieves items from the queue and stores them.
    """

    def __init__(self, destination, queue):
        """
        :param destination: List to store consumed Product objects.
        :param queue: The BlockingQueue instance for data transfer.
        """
        super().__init__(name="ConsumerThread")
        self.destination = destination
        self.queue = queue

    def run(self):
        # Runs continuously until a sentinel END product is received.

        while True:
            product = self.queue.take()
            print(f"[Consumer] Consuming: {product}")
            self.destination.append(product)

            if product.product_id == "END":
                print("[Consumer] END product received. Stopping consumer.")
                break
