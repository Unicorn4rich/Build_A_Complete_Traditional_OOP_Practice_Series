# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. 
# Define a __call__() method that multiplies an input by the factor.
# Test it with callable() and by calling the object like a function.



class Multiplier:
  def __init__(self, factor):
    self.factor_num = factor

  def __call__(self, input_val):
    return input_val * self.factor_num  


machine = Multiplier(5)
print(callable(machine)) # True

machine.factor_num
machine(10) # 50