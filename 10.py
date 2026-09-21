# list operations

#1. looping through a list
l = [10, 20, 30, 40, 50]

for x in l:
    print(x) # it will print all the elements of the list one by one

#loop using index
for i in range(0, len(l)):
    print(l[i]) # it will print all the elements of the list one by one
    #range function takes 3 arguments : start, end, step


# sort 
l=[50, 20, 30, 10, 40]
l.sort() # sorting the list in ascending order
print(l) # [10, 20, 30, 40, 50]
#descending order
l.sort(reverse=True) # sorting the list in descending order
print(l) # [50, 40, 30, 20, 10]

#reverse a list
l=[10, 20, 30, 40, 50]
l.reverse() # reversing the list
print(l) # [50, 40, 30, 20, 10]

l=[10, 20, 30, 40, 50]
#finding the index of an element in a list
print(l.index(30)) # 2 : it will return the index of the first occurrence

print(l.count(20)) # 1 : it will return the number of occurrences of the element in the list



numbers = [10, 20, 30, 40]

print(min(numbers))   # 10
print(max(numbers))   # 40
print(sum(numbers))   # 100

# how to take list as input from user

numbers = list(map(int,input().split()))

# user enters 10 20 30 40  
# input() takes the entire input as a string "10 20 30 40"
# .split() by default splits the string by space and returns a list of strings ['10', '20', '30', '40']

# map(int, ...)  Applies int() to every element:
#so conceptually we get 10,20,30,40
#map() gives a map object, so we convert it into a list:

#in python map is not a data structure but it is built-in function that applies a function to every element of an iterable  


# LIST CONCTENATION
l1 = [1, 2, 3]
l2 = [4, 5, 6]
l3 = l1 + l2 # concatenating two lists

a = [1, 2, 3]
print(a * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3] : repeating the list 3 times
print(a) # [1, 2, 3] : original list is not modified


#LIST COMPREHENSION : it is a concise way to create lists
#syntax : [expression for item in iterable if condition]

list = []

for i in range(1,11):
    if i % 2 == 0:
        list.append(i**2) # adding even numbers to the list
   

# equivalent list comprehension
list = [i**2 for i in range(1,11) if i % 2 == 0] # adding even numbers to the list