# 9. Abstract Classes and Methods
# Assignment:
# Use the abc module to create an abstract class Shape with an abstract method area().
# Inherit a class Rectangle that implements area().

from abc import ABC, abstractmethod


class Shape(ABC):

  @abstractmethod
  def area(self):
    pass


class Rectangle(Shape):
  def area(self):
    print("this is bara area")


rectangle= Rectangle()

rectangle.area()

