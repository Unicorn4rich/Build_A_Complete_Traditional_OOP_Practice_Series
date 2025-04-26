# 18. Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. 
# Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.


class Product:
  def __init__(self, price):
    self.__price = price

  @property
  def price(self):
    return self.__price

  @price.setter
  def price(self, update_pr):
    self.__price = update_pr

  @price.deleter
  def price(self):
    del self.__price  



product = Product(3000)

product.price
product.price = 150
product.price
del product.price





