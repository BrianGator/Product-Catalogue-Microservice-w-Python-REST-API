import unittest
import threading
from service import app

def simulate_heavy_load(client):
    for _ in range(50):
        client.get("/products")

class TestStress(unittest.TestCase):
    def test_concurrent_db_stress(self):
        """Stress the DB with 10 simultaneous threads"""
        client = app.test_client()
        threads = []
        for _ in range(10):
            t = threading.Thread(target=simulate_heavy_load, args=(client,))
            threads.append(t)
            t.start()
        
        for t in threads:
            t.join()
        
        # Verify system is still responsive
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
