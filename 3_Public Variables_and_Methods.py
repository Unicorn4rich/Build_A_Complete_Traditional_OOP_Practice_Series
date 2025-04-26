# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class


class Car:
  brand = "Toyota"

  def start(self):
    return print(f"Car engine started")


car = Car()
print(car.brand)
car.start()
