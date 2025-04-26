# 14. Aggregation
# Assignment:
# Create a class Department and a class Employee. 
# Use aggregation by having a Department object store a 
# reference to an Employee object that exists independently of it.


# employe class
class Employe:
  def __init__(self):
    self.name = "shoaib"

employe = Employe()


# department class
class Department:
  
  def __init__(self, employe):
    self.job_dep = "Manager"
    self.employe = employe

department = Department(employe)
print("from Employe:", department.employe.name)


