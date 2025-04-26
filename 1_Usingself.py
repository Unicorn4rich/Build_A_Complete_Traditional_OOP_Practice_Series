# 1. Using self
# Assignment:
# Create a class Student with attributes name and marks. 
# Use the self keyword to initialize these values via a constructor. 
# Add a method display() that prints student details.


class Student:
  def __init__(self, name: str, marks: int):
    self.name = name
    self.marks = marks

  def display(self):
    return print(f"Student name is: {self.name}, and age: {self.marks}")


student = Student("shoaib", 23) 
student.display()
