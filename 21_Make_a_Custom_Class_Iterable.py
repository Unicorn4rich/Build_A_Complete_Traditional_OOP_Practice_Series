# 21. Make a Custom Class Iterable
# Assignment:
# Create a class Countdown that takes a start number. 
# Implement __iter__() and __next__() to make the 
# object iterable in a for-loop, counting down to 0.


class Countdown:
  def __init__(self, start_num):
    self.start_num = start_num 

  def __iter__(self):
    return self

  def __next__(self):
    if self.start_num < 0:
      raise StopIteration
    else:
      val = self.start_num
      self.start_num -= 1
      return val  


countdown = Countdown(10)    
for num in countdown:
  print(num)