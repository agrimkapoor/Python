# functions

def f(a,b): #parameters
    return a+b

ans = f(5,10) #arguements 
print(ans)

# if we want to tell ki func int return karega

def f2(a,b) -> int:
    return a+b

print(f2(5,10))

# specify the datatype of parameters
#Python mein : int type hint hai; Python automatically force nahi karta ki argument int hi ho.
def f3(a: int, b: int) -> int:
    return a + b


# if the return value can be int or float

def f4 (a : int,b:int)->int|float:
    return a/b

# if the parameters can be int or float

def f5(a:int|float,b:int|float)->int|float:
    return a + b

#multiple return values 
def calculate(a, b):
    return a + b, a - b

x, y = calculate(10, 5)

print(x)
print(y)

#default parameters
def greet(name="User"):
    print("Hello", name)

greet()
greet("Agrim")

#keyword arguements
def student(name, age):
    print(name, age)

student(age=21, name="Agrim")# we can specify which parameter gets which value
#now position not matters


# *args : allows us to pass any number of positional arguements
def add(*numbers):
    sum = 0

    for x in numbers:
        sum += x

    return sum

print(add(10, 20))
print(add(10, 20, 30))
print(add(1, 2, 3, 4, 5))


# **kwargs : allows us to pass multiple keyword arguements

def student(**data):
    print(data)

student(name="Agrim", age=21, branch="CSE")
#{'name': 'Agrim', 'age': 21, 'branch': 'CSE'}
# inside the function data behaves as a dictionary