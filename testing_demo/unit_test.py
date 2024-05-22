import unittest

class Product:
  def __init__(self, name, price, quantity):
    self.name = name
    self.price = price
    self.quantity = quantity

  def calculateTotal(self):
    if self.quantity < 0:
        raise ValueError("Quantity cannot be negative")
    return self.price * self.quantity



class TestProduct(unittest.TestCase):
  def test_calculateTotal_positive(self):
    product = Product("T-Shirt", 10.0, 2)
    total = product.calculateTotal()
    self.assertEqual(total, 20.0)
    
  def test_calculateTotal_zero_quantity(self):
    product = Product("Mug", 5.0, 0)
    total = product.calculateTotal()
    self.assertEqual(total, 0.0)

  def test_calculateTotal_negative_quantity(self):
    product = Product("Hat", 15.0, -1)
    with self.assertRaises(ValueError):  # Test for expected error
      total = product.calculateTotal()

if __name__ == "__main__":
    unittest.main()