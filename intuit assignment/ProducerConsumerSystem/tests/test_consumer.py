import unittest
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from producer_consumer.pc_queue.blocking_queue import BlockingQueue
from producer_consumer.threads.consumer import Consumer
from producer_consumer.models.product import Product


class TestConsumer(unittest.TestCase):

    def test_consumer_consumes_until_end(self):
        """Consumer must consume items until receiving END sentinel."""
        q = BlockingQueue(10)
        destination = []

        q.put(Product("A"))
        q.put(Product("B"))
        q.put(Product("END"))

        c = Consumer(destination, q)
        c.start()
        c.join()

        ids = [p.product_id for p in destination]
        self.assertEqual(ids, ["A", "B", "END"])
