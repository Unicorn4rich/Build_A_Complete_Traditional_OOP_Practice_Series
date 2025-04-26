# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.


class MathUtils:

  @staticmethod
  def add(a: int, b: int):
    return a + b


mathUtils = MathUtils() 
print(mathUtils.add(23, 7)) 