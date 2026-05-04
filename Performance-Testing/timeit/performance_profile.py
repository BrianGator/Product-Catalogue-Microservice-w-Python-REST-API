import timeit
from decimal import Decimal

# Code to measure: Decimal conversion vs Float (Data Integrity check)
def test_decimal_precision():
    Decimal("123.456789") * Decimal("1.2")

def test_float_precision():
    123.456789 * 1.2

if __name__ == "__main__":
    decimal_time = timeit.timeit(test_decimal_precision, number=1000000)
    float_time = timeit.timeit(test_float_precision, number=1000000)

    print(f"Decimal (1M ops): {decimal_time:.4f}s")
    print(f"Float (1M ops): {float_time:.4f}s")
