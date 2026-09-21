#TUPLES in python : it is also a collection of items but it is immutable (we cannot change the elements of a tuple once it is created)

#1. Creating a tuple : it is done by using parentheses () and separating the items with commas

numbers = (1, 2, 3, 4, 5) # tuple of integers
print(numbers) # (1, 2, 3, 4, 5)

# if you have data that should not change, you should use a tuple instead of a list. Tuples are faster than lists.

x = (10,20)
print(type(x)) # <class 'tuple'>

x=(10)
print(type(x)) # <class 'int'> : it is not a tuple, it is an integer

x=(10,) # single element tuple : we need to add a comma after the element to make it a tuple


# Tuple unpacking : it is the process of assigning the elements of a tuple to variables
student = ("Agrim", 21, "CSE")

name, age, branch = student

print(name)
print(age)
print(branch)

#List unpacking
numbers = [10,20,30]
a,b,c = numbers

numbers = [10,20,30,40,50]
a,*b,c = numbers
print(a) #10
print(b) #[20,30,40]
print(c)# 50