from locust import HttpUser, task, between

class ProductServiceUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def list_products(self):
        """Simulate users browsing the catalogue"""
        self.client.get("/products")

    @task(3)
    def view_product(self):
        """Simulate users viewing specific product details (more frequent)"""
        # Assuming product ID 1 exists for simulation
        self.client.get("/products/1")

    @task(1)
    def create_product(self):
        """Simulate an admin adding a new product occasionally"""
        self.client.post("/products", json={
            "name": "Locust Product",
            "description": "Load test generated",
            "price": "19.99",
            "available": True,
            "category": "TOOLS"
        })
