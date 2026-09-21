# LOOPS in python : for and while 

i=0
while i<5 :
    print(i,end=" ")
    i+=1 # dont forget this

numbers = [10,20,30,40]
for x in numbers : 
    print(x,end=" ")

s = "Hello"
for ch in s:
    print(ch,end=" ")

for i in range(5):
    print(i,end=" ") # 0 to 4

for i in range(2,6):
    print(i,end=" ") # 2 to 5

for i in range(0,10,2):
    print(i,end=" ") # 0 2 4 6 8

for i in range(5,0,-1): #negative step mei start > end
    print(i,end=" ")


#break

for i in range(10):
    if i==5 :
        break
    print(i,end=" ") # 0 1 2 3 4

#continue
for i in range(5):
    if i==2 :
        continue
    print(i) # 0 1  3 4 

#pass : do nothing
l=[]
for i in range(5):
    if i == 2:
        pass # kuch mat karo , it is a placeholder statement
    else :
        l.append(i)
    print(i,end=" ") #  0 1 2 3 4

print(l)