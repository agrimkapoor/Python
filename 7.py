# string operations in python

str1 = "Hello"
str2 = "World"

# string concatenation
str3 = str1 + " " + str2
print(str3)

# length of string
print(len(str1))

str = "This is line 1 .\nThis is line 2"
print(str) # \n is used to print in new line


s="Hello"
print(s[0]) # H
# s[2]='i' # this will give error because string is immutable in python, we cannot change the value of string after it is created

#Slicing : accessing parts of a string
# s[start:end] : it will give the string from start index to end-1 index
print(s[0:3]) # Hel 
print(s[1:]) # ello this is same as s[1:len(s)]
print(s[:3]) # Hel this is same as s[0:3]

#slicing with negative index
# Apple = -5 -4 -3 -2 -1
s = "Apple"
print(s[-1]) # e
print(s[-3:-1])#pl
print(s[2:-1])#pl


s = "Hello World"

print(s.upper()) # HELLO WORLD
print(s.lower()) # hello world
print(s.endswith("ld")) # True
print(s.startswith("He")) # True

s ="hello world this is PYTHON "
print(s.capitalize()) # Hello world this is python # capitalize() method capitalizes the first letter of the string and makes all other letters lowercase

s = s.upper() # ab original string mei modification
# s.upper() method returns a new string with all characters in uppercase, but it does not modify the original string. To modify the original string, we need to assign the result back to the variable, as done here.

s="Python is a programming language"
print(s.replace("Python","Java")) # Java is a programming language  # koi bhi substring ko replace karne ke liye use hota hai, ye bhi original string ko modify nhi karta hai, ye ek new string return karta hai

print(s.find("programming")) # 10 : it will return the index of the first occurrence of the substring, if not found it will return -1

print(s.count("a")) # 3 : it will return the number of occurrences of the substring in the string

print(s.split(" ")) # ['Python', 'is', 'a', 'programming', 'language'] : it will split the string into a list of substrings based on the delimiter provided, in this case space

s = "HelloWorld"

print(s[1:8:2]) # elW # the third parameter in slicing is the step, it will take every 2nd character from index 1 to 7

#reverse a string
s = "Hello World"
print(s[::-1]) # dlroW olleH : it will reverse the string
#why this is working : s[start:end:step] : if we don't provide start and end it will take the whole string, and step is -1 so it will take every character from the end to the start

#s[start:end:step]  start <= end if step is positive, start >= end if step is negative