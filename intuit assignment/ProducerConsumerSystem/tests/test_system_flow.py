import unittest
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from producer_consumer.pc_queue.blocking_queue import BlockingQueue
from producer_consumer.threads.producer import Producer
from producer_consumer.threads.consumer import Consumer
from producer_consumer.models.product import Product


class TestSystemFlow(unittest.TestCase):

    def test_full_producer_consumer_pipeline(self):
        """End-to-end flow: all produced items must be consumed."""
        source = [
            Product("P1"),
            Product("P2"),
            Product("P3"),
            Product("END")
        ]
        dest = []
        q = BlockingQueue(2)

        prod = Producer(source, q)
        cons = Consumer(dest, q)

        prod.start()
        cons.start()

        prod.join()
        cons.join()

        ids = [p.product_id for p in dest]
        self.assertEqual(ids, ["P1", "P2", "P3", "END"])
