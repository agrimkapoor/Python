# LISTS IN PYTHON

# list is a collection of items used to store multiple items in a single variable

#1.Creating a list : it is done by using square brackets [] and separating the items with commas

marks = [90, 80, 70, 60, 50] # list of integers
print(marks) # [90, 80, 70, 60, 50]

# it can also contain different data types
mixed_list = [1, "Hello", 3.14, True] # list of different data types

#2. Accessing Elements in a list 
l = [10, 20, 30, 40, 50]

print(l[0]) # 10 : accessing the first element of the list
print(l[-2]) # 40 : accessing the second last element of the list

#3. changing an element in a list : LISTS ARE MUTABLE BUT STRING WASNT
l[2] = 35 # changing the third element of the list
print(l) # [10, 20, 35, 40, 50]


#4. List Slicing : accessing parts of a list
l=[10, 20, 30, 40, 50]
#list[start:end] : it will give the list from start index to end-1 index
print(l[1:4]) # [20, 35, 40] : accessing

#5. to find length
print(len(l)) # 5 : length of the list

#6. Adding elements to a list
l=[10, 20, 30, 40, 50]
l.append(60) # adding an element at the end of the list
print(l) # [10, 20, 35, 40, 50, 60]

names = ["Alice", "Bob", "Charlie"]
names.append("David") # adding an element at the end of the list

#inserting an element at a specific index  (index, element)
names.insert(1, "Eve") # inserting "Eve" at index 1
print(names) # ['Alice', 'Eve', 'Bob', 'Charlie', 'David']

#adding multiple elements to a list
numbers = [1, 2, 3]
numbers.extend([4, 5, 6]) # adding multiple elements to the list
print(numbers) # [1, 2, 3, 4, 5, 6]

numbers = [1,2,3]
numbers.append([4,5,6]) # adding a list as a single element to the list
print(numbers) # [1, 2, 3, [4, 5, 6]] : it will add the list as a single element to the list


#7. Removing elements from a list
l=[10, 20, 30, 40, 50]
l.remove(30) # removing an element from the list #ye function will not return any value, it will just remove the element from the list
print(l) # [10, 20, 40, 50]

#removing an element at a specific index from the list
l=[10, 20, 30, 40, 50]
l.pop(2) # removing an element at a specific index from the list
print(l) # [10, 20, 40, 50]

# removing a part of list using slicing
del l[1:3] # removing elements from index 1 to 2


#membership operator : to check if an element is present in the list or not
numbers=[10, 20, 30, 40, 50]
print(30 in numbers) # True
print(60 in numbers) # False

print(30 not in numbers) # False
print(60 not in numbers) # True

s = "Agrim"

print("gr" in s) # True : it will check if the substring is present in the string or not
