# file input/output or file i/o means reading and writing data to a file 

# open a file
#file = open("filename.txt","mode")


# file modes
# "r"	Read
# "w"	Write
# "a"	Append
# "x"	Create new file
# "rb"	Read binary --> BINARY FILE MEI READ
# "wb"	Write binary

# if the file already has content w erases the old content

# data.txt contains 
    # HELLO
    # WORLD
    # PYTHON

#READING A FILE
file = open("data.txt","r")
data = file.read()
print(data)
print(type(data)) # ek string hai
file.close()

# READING A FILE LINE BY LINE
file = open("data.txt","r")
lines = file.readlines() # reads all line and stores them in a list
print(lines) #['HELLO\n', 'WORLD\n', 'PYTHON']
print(type(lines)) #list
file.close()

#1.BETTER APPROACH TO READ A FILE : USE WITH AS IT AUTOMATICALLY CLOSES THE FILE AFTER THE WORK IS DONE
with open("data.txt","r") as file:
    content = file.read()
    print(content)
#2. WRITING TO A FILE
with open("data.txt","w") as file :
    file.write("Hello Python")
#3. APPENDING TO A FILE
with open("data.txt","a")as file:
    file.write("\n New Line added")
