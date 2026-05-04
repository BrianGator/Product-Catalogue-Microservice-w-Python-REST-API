import unittest
from service import app

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_to_get_lifecycle(self):
        """Integration: Create a product and then retrieve it by ID"""
        payload = {"name": "Integrated Prod", "description": "test", "price": "25.00", "available": True, "category": "TOOLS"}
        create_res = self.client.post("/products", json=payload)
        self.assertEqual(create_res.status_code, 201)
        pid = create_res.get_json()["id"]
        
        get_res = self.client.get(f"/products/{pid}")
        self.assertEqual(get_res.status_code, 200)
        self.assertEqual(get_res.get_json()["name"], "Integrated Prod")

    def test_create_update_get_lifecycle(self):
        """Integration: Create, update details, then verify changes"""
        payload = {"name": "Old Name", "description": "test", "price": "10.00", "available": True, "category": "TOOLS"}
        create_res = self.client.post("/products", json=payload)
        pid = create_res.get_json()["id"]
        
        update_payload = {"name": "New Name", "description": "test", "price": "15.00", "available": False, "category": "BOOKS"}
        self.client.put(f"/products/{pid}", json=update_payload)
        
        get_res = self.client.get(f"/products/{pid}")
        data = get_res.get_json()
        self.assertEqual(data["name"], "New Name")
        self.assertEqual(data["category"], "BOOKS")

    def test_create_and_delete_lifecycle(self):
        """Integration: Create product and delete it, ensuring it's gone"""
        payload = {"name": "Delete Me", "description": "test", "price": "1.00", "available": True, "category": "TOOLS"}
        create_res = self.client.post("/products", json=payload)
        pid = create_res.get_json()["id"]
        
        del_res = self.client.delete(f"/products/{pid}")
        self.assertEqual(del_res.status_code, 204)
        
        get_res = self.client.get(f"/products/{pid}")
        self.assertEqual(get_res.status_code, 404)

    def test_list_and_filter_integration(self):
        """Integration: Create multiple and filtered search"""
        self.client.post("/products", json={"name": "A", "description": "D", "price": "1.0", "available": True, "category": "TOOLS"})
        self.client.post("/products", json={"name": "B", "description": "D", "price": "2.0", "available": False, "category": "TOOLS"})
        
        res = self.client.get("/products?category=TOOLS&available=true")
        data = res.get_json()
        self.assertTrue(len(data) >= 1)
        self.assertEqual(data[0]["name"], "A")

    def test_bad_payload_persistence_rejection(self):
        """Integration: Verify invalid model data is rejected before DB commit"""
        payload = {"name": "MissingFields"} # Price/Category missing
        response = self.client.post("/products", json=payload)
        self.assertEqual(response.status_code, 400)

    def test_idempotent_deletion(self):
        """Integration: Verify deleting same ID twice is handled correctly"""
        pid = 9999
        res1 = self.client.delete(f"/products/{pid}")
        res2 = self.client.delete(f"/products/{pid}")
        # Depending on spec 204 or 404, but should not crash
        self.assertIn(res1.status_code, [204, 404])
        self.assertIn(res2.status_code, [204, 404])
