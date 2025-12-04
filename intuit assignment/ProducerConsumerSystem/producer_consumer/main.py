from pc_queue.blocking_queue import BlockingQueue
from threads.producer import Producer
from threads.consumer import Consumer
from models.product import Product


def main():
    """
    Initializes and runs the producer–consumer workflow.
    Includes error handling for invalid configuration and runtime failures.
    """
    try:
        # Queue capacity validation (exception raised inside BlockingQueue)
        queue = BlockingQueue(capacity=2)

        # Define product stream
        source_products = [
            Product("A1"),
            Product("B2"),
            Product("C3"),
            Product("END")
        ]

        destination_products = []

        producer = Producer(source_products, queue)
        consumer = Consumer(destination_products, queue)

        producer.start()
        consumer.start()

        producer.join()
        consumer.join()

        print("\n=== Final Consumed Products ===")
        for product in destination_products:
            print(product)

    except ValueError as ve:
        # Handles invalid capacity or invalid product issues
        print(f"[ERROR] Configuration Error: {ve}")

    except Exception as e:
        # Handles unexpected runtime exceptions
        print(f"[ERROR] An unexpected error occurred: {e}")

    finally:
        # Always executes (success or failure)
        print("\n[INFO] System shutting down...")


if __name__ == "__main__":
    main()
