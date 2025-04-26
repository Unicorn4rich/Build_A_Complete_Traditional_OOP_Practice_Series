# 20. Creating a Custom Exception
# Assignment:
# Create a custom exception InvalidAgeError. 
# Write a function check_age(age) that raises this exception if age < 18.
# Handle it with try...except.


class InvalidAgeError(Exception):
  def __init__(self, message="You are underage, try later"):
    self.message = message
    super().__init__(self.message)


def check_age(age):
  if age >= 18:
    print(f"Congratulations your age is: {age}")
  elif age < 18:
    raise InvalidAgeError() 


try:
  check_age(2)
except InvalidAgeError as e:
  print("Error", e)  