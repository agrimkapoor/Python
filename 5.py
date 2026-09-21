#type conversion in python 

#type conversion is the process of converting one data type to another data type

#implicit type conversion
#python automatically converts one data type to another data type

a=5 #int
b=2.5 #float
sum=a+b #python automatically converts int to float and then adds them

#explicit type conversion : this is known as type casting 

#we can use built-in functions to convert one data type to another data type

x = "25"

y = int(x)

print(y)        # 25
print(type(y))  # <class 'int'>
