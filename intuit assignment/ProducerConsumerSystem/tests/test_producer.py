import unittest
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from producer_consumer.pc_queue.blocking_queue import BlockingQueue
from producer_consumer.threads.producer import Producer
from producer_consumer.models.product import Product


class TestProducer(unittest.TestCase):

    def test_producer_produces_all_items(self):
        """Producer must deliver all products to the queue."""
        q = BlockingQueue(10)
        source = [Product("A"), Product("B"), Product("END")]

        p = Producer(source, q)
        p.start()
        p.join()

        # Validate order
        self.assertEqual(q.take().product_id, "A")
        self.assertEqual(q.take().product_id, "B")
        self.assertEqual(q.take().product_id, "END")
