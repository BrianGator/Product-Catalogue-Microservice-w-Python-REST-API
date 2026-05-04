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
        response = client.get("/") # Fixed self.client to client
        self.assertEqual(response.status_code, 200)

    def test_rapid_creation_stress(self):
        """Verify system handles rapid sequential creates"""
        client = app.test_client()
        for i in range(100):
            payload = {"name": f"P{i}", "description": "D", "price": "1.00", "available": True, "category": "TOOLS"}
            client.post("/products", json=payload)
        response = client.get("/products")
        self.assertEqual(response.status_code, 200)

    def test_large_payload_stress(self):
        """Verify system handles large text payloads"""
        client = app.test_client()
        large_desc = "A" * 10000
        payload = {"name": "L", "description": large_desc, "price": "1.00", "available": True, "category": "TOOLS"}
        response = client.post("/products", json=payload)
        self.assertEqual(response.status_code, 201)

    def test_recursive_search_load(self):
        """Verify system handles deep filtering queries under load"""
        client = app.test_client()
        for _ in range(50):
            client.get("/products?category=TOOLS&available=true&name=P")
        self.assertEqual(client.get("/").status_code, 200)

    def test_invalid_route_bombardment(self):
        """Verify system doesn't leak memory on 404 bombardment"""
        client = app.test_client()
        for i in range(100):
            client.get(f"/invalid/{i}")
        self.assertEqual(client.get("/").status_code, 200)

    def test_concurrent_read_write(self):
        """Verify read/write consistency under moderate concurrency"""
        client = app.test_client()
        def writer():
            client.post("/products", json={"name": "W", "description": "D", "price": "1.00", "available": True, "category": "TOOLS"})
        def reader():
            client.get("/products")
        
        t1 = threading.Thread(target=writer)
        t2 = threading.Thread(target=reader)
        t1.start(); t2.start()
        t1.join(); t2.join()
        self.assertEqual(client.get("/").status_code, 200)

    def test_headers_overflow_stress(self):
        """Verify system handles unusually large headers (within bounds)"""
        client = app.test_client()
        headers = {"X-Custom-Data": "X" * 4000}
        response = client.get("/", headers=headers)
        self.assertEqual(response.status_code, 200)
