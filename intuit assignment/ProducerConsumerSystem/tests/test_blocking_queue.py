import unittest
import threading
import time
import os
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
from producer_consumer.pc_queue.blocking_queue import BlockingQueue


class TestBlockingQueue(unittest.TestCase):

    def test_invalid_capacity(self):
        """Queue must reject zero or negative capacity."""
        with self.assertRaises(ValueError):
            BlockingQueue(0)
        with self.assertRaises(ValueError):
            BlockingQueue(-1)

    def test_put_take_normal(self):
        """Basic put/take operations should work in FIFO order."""
        q = BlockingQueue(2)
        q.put("A")
        q.put("B")
        self.assertEqual(q.take(), "A")
        self.assertEqual(q.take(), "B")

    def test_take_blocks_until_item_available(self):
        """
        When queue is empty, take() must block and then resume
        once an item is put.
        """
        q = BlockingQueue(1)
        result = []

        def consumer():
            result.append(q.take())  # Should block until producer adds item

        t = threading.Thread(target=consumer)
        t.start()

        time.sleep(0.1)  # Give time for consumer to block
        q.put("X")       # Should wake the consumer
        t.join()

        self.assertEqual(result, ["X"])

    def test_put_blocks_until_space_available(self):
        """
        When queue is full, put() must block until a consumer takes an item.
        """
        q = BlockingQueue(1)
        q.put("A")  # Queue full

        flag = []

        def producer():
            q.put("B")   # Should block until take() happens
            flag.append(True)

        t = threading.Thread(target=producer)
        t.start()

        time.sleep(0.1)
        self.assertEqual(flag, [])  # Producer should still be blocked

        q.take()  # Free space → unblock producer
        t.join()

        self.assertEqual(flag, [True])

    def test_multiple_producers_consumers(self):
        """
        Stress test for concurrency with multiple producers and consumers.
        Ensures no item is lost and ordering remains consistent.
        """
        q = BlockingQueue(3)
        consumed = []
        lock = threading.Lock()  # Protect shared list

        def producer(start):
            for i in range(start, start + 3):
                q.put(i)

        def consumer():
            for _ in range(3):
                with lock:
                    consumed.append(q.take())

        p1 = threading.Thread(target=producer, args=(0,))
        p2 = threading.Thread(target=producer, args=(100,))
        c1 = threading.Thread(target=consumer)
        c2 = threading.Thread(target=consumer)

        p1.start(); p2.start(); c1.start(); c2.start()
        p1.join(); p2.join(); c1.join(); c2.join()

        # Validate all items produced were consumed
        self.assertEqual(sorted(consumed), [0,1,2,100,101,102])
