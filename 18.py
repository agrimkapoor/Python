#OOPS IN PYTHON

class Student :
  name = "Agrim" #yahi pe value dedo
  age = "21" #these are class attributes

student1 = Student()
print(student1.name)

#constructor in python
class Student :
  def __init__(self,name,age): # self refers to the current object
    self.name = name # ye attribute ban jaayega and this attribute will belong to the instance
    self.age = age

# methods
class Student:
  def __init__(self,name):
    self.name = name
  def f(self):
    print(self.name)


# static methods : isme self nhi jaayega as it belongs to class
class Calculator:

    @staticmethod # this is a decorator which tells python to treat the following function as static
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
