# 12. Static Methods
# Assignment:
# Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c)
# that returns the Fahrenheit value.



class TemperatureConverter:

  @staticmethod
  def celsius_to_fahrenheit(C):
    return (C * 9/5) + 32


tp_fahrenheit = TemperatureConverter()
print(f"The fahrenheit is: {tp_fahrenheit.celsius_to_fahrenheit(7)}")