# Set : it is a collection of unique elements and keeps not in sorted (unordered sets), remove duplicates on own

numbers = {10, 20, 20, 30, 30, 30}

print(numbers) # {10,20,30}

x={} # this is not empty set but empty dictionary


#set is unordered : you cant do numbers[0]

A = {1, 2, 3}
B = {3, 4, 5}

print(A | B) #union
print(A & B) # intersection
print(A - B) # difference : elements present in A but not in B
print( A ^B) # symmetric difference : ya toh A mei ya B mei par dono mei nhi

numbers = {10,20,30}

for x in numbers:
    print(x)

# removing elements
numbers = {10, 20, 30}

numbers.remove(20)

print(numbers) #{10,30}

numbers.add(15)
print(numbers)#{10,30,15} sorted nhi rehega
