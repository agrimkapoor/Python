# operators in python

# Arithmetic Operators
a = 10
b = 3
print("Addition:", a + b) # Addition: 13
print("Subtraction:", a - b) # Subtraction: 7
print("Multiplication:", a * b) # Multiplication: 30

print("Division:", a / b) # Division: 3.3333333333333335
print("Floor Division:", a // b) # Floor Division: 3

print("Modulus:", a % b) # Modulus: 1
print("Exponentiation:", a ** b) # Exponentiation: 1000

# Comparison Operators
x = 5
y = 10
print("Equal to:", x == y) # Equal to: False
print("Not equal to:", x != y) # Not equal to: True

print("Greater than:", x > y) # Greater than: False
print("Less than:", x < y) # Less than: True
print("Greater than or equal to:", x >= y) # Greater than or equal to: False
print("Less than or equal to:", x <= y) # Less than or equal to: True

# Logical Operators
p = True
q = False
print("Logical AND:", p and q) # Logical AND: False
print("Logical OR:", p or q) # Logical OR: True
print("Logical NOT:", not p) # Logical NOT: False : it is !p in c++  

# Assignment Operators
c = 5
c += 3
c -= 2
c *= 4

c /= 6
c %= 3  
c **= 2



# Bitwise Operators
m = 5  # binary: 0101
n = 3  # binary: 0011
print("Bitwise AND:", m & n)  # Bitwise AND: 1 (binary: 0001)
print("Bitwise OR:", m | n)   # Bitwise OR: 7 (binary: 0111)
print("Bitwise XOR:", m ^ n)  # Bitwise XOR: 6 (binary: 0110)
print("Bitwise NOT:", ~m)      # Bitwise NOT: -6 (binary: 1010, two's complement representation)
print("Left Shift:", m << 1)   # Left Shift: 10 (binary: 1010)
print("Right Shift:", m >> 1)  # Right Shift: 2 (binary : 0010) 

