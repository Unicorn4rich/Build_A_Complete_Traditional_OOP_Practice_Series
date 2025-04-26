# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.



class Employee:

  def __init__(self):
    self.name = "Shoaib"
    self._salery = 25
    self.__ssn = "sho2133"


  def getter(self):
    return self.__ssn


employee = Employee()

print(employee.name)
print(employee._salery)
print(employee.getter())

