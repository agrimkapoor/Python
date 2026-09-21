# dictionary in python {}

student = {
    "name": "Agrim",
    "age": 21,
    "branch": "CSE"
}

print(student["name"]) # "name" likhna hoga
print(student["age"])

#adding a new key value pair
student["marks"]=90

#updating a value
student["age"]=22

#keys in dictionary must be unique

#check whether a key exists
student = {
    "name": "Agrim",
    "age": 21,
    "branch": "CSE"
}

print("name" in student) #True
# it not check values
print("Agrim" in student) # False

student = {
    "name": "Agrim",
    "age": 21,
    "branch": "CSE"
}

#print(student["marks"]) This give error if key not exists

print(student.get("name")) #Agrim
print(student.get("marks")) #None as key not exists

#remove elements by using key

student.pop("age")
print(student)

student.clear() #removes all the keys
print(student) #{} empty


# get all the keys
student = {
    "name": "Agrim",
    "age": 21,
    "branch": "CSE"
}

print(student.keys())

for key in student.keys() :
    print(key,end=" ")

for key in student : # this also give keys
    print(key)

# getting all values
for value in student.values():
    print(value)

# getting all elements(key value pair)
for key,value in student.items():
    print(key,value,sep=" ")


# taking dictionary as input 
numbers = [1, 2, 2, 3, 1, 2]
# we have to maintain freq of each distinct el

freq={}
for x in numbers :
    if x in freq:
        freq[x] += 1
    else :
        freq[x] = 0

# dictionary comprehension
squares = {}

for i in range(5):
    squares[i] = i * i