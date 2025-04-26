# 2. Using cls
# Assignment:
# Create a class Counter that keeps track of how many objects have been created. 
# Use a class variable and a class method with cls to manage and display the count.


class Counter:
  var_counts = 0

  def __init__(self):
    Counter.var_counts += 1

  @classmethod
  def lazy(cls): # cls => ye self ki tarhn kaam karta hai
    print(f"Total object number: {cls.var_counts}")


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()

counter1.lazy() # Total object number: 4