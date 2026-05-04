import pytest
from service import app
from service.models import Product
from tests.factories import ProductFactory

def test_list_products_benchmark(benchmark):
    """Benchmark the GET /products endpoint"""
    client = app.test_client()
    
    # Use benchmark fixture to measure execution time
    result = benchmark(client.get, "/products")
    assert result.status_code == 200
