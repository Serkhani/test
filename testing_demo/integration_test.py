import unittest

from unit_test import Product

class ShoppingCart:
  def __init__(self):
    self.cart = []

  def addProduct(self, product):
    self.cart.append(product)

  def getCartTotal(self):
    total = 0
    for item in self.cart:
      total += item.calculateTotal()
    return total


class TestShoppingCart(unittest.TestCase):
  def test_getCartTotal_empty_cart(self):
    cart = ShoppingCart()
    total = cart.getCartTotal()
    self.assertEqual(total, 0.0)

  def test_getCartTotal_with_products(self):
    cart = ShoppingCart()
    cart.addProduct(Product("Shirt", 20.0, 1))
    cart.addProduct(Product("Book", 10.0, 2))
    total = cart.getCartTotal()
    self.assertEqual(total, 40.0)

if __name__ == "__main__":
  unittest.main()
