# OOPS continued

class Student:
    def __init__(self, name):
        self.name = name # public attribute

student = Student("Agrim")
print(student.name)

# for private attribute : use double underscore

class Student :
  def __init__(self,name,age):
    self.name = name
    self.__age = age
    
student = Student("Agrim",21)
print(student.name)     # Works
#print(student.__age)    THIS WILL GIVE ERROR

class Student:
    def __init__(self, age):
        self.__age = age

    @property # this decorator makes a function behave like a attribute
    def age(self):
        return self.__age
      
student = Student(20)
print(student.age) # now we are able to do thi


class Student:
    def __show_marks(self): # PRIVATE METHOD
        print("Marks: 90")


student = Student()

# student.__show_marks() THIS GIVES ERROR




# INHERITANCE 
class Animal:
    def eat(self):
        print("Animal is eating")


class Dog(Animal):
    def bark(self):
        print("Dog is barking")


dog = Dog()

dog.eat()
dog.bark()


# SUPER METHOD : IT IS USED TO CALL THE PARENT KA METHOD

class Animal:
    def speak(self):
        print("Animal makes a sound")


class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog says Woof")


dog = Dog()

# dog.speak() 
# Animal makes a sound
# Dog says Woof



# A class method gets access to the class (cls). A static method gets neither the class nor the object automatically.STATIC METHOD NOT GETS self or cls
class Student:
    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()


