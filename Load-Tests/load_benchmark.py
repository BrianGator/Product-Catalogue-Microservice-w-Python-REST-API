import time
import unittest
from service import app

class TestLoad(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_response_time_benchmark(self):
        """Ensure listing products takes less than 50ms"""
        start_time = time.time()
        for _ in range(100):
            self.client.get("/products")
        end_time = time.time()
        avg_time = (end_time - start_time) / 100
        print(f"Average Response Time: {avg_time:.4f}s")
        self.assertLess(avg_time, 0.050)
