# Operators
#1. Arithmetic Operators
a = 10
b = 5
print("Addition:", a + b)        # Output: 15
print("Subtraction:", a - b)     # Output: 5
print("Multiplication:", a * b)  # Output: 50
print("Modulus:", a % b)         # Output: 0

#2. Comparison Operators - Boolean Value Output
x = 10
y = 20
print("Greater than:", x > y)    # Output: False
print("Less than:", x < y)       # Output: True
print("Equal to:", x == y)       # Output: False
print("Not equal to:", x != y)   # Output: True

#3. Assignment Operators
c = 10

#4. Logical Operators
p = 15
q = 30
print(p==15 and q==30)  # Output: True
print(p==15 or q>20)   # Output: True
print(not(p==15 and q==30))  # Output: False

#5. Identity Operators - is and is not
q = [1, 2, 3]
r = q
s = [1, 2, 3]
print(q is r)  # Output: True
print(q is s)  # Output: False
print(q is not s)  # Output: True

#6. Membership Operators - in and not in
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)  # Output: True
print(6 in my_list)  # Output: False
print(6 not in my_list)  # Output: True

#7. Bitwise Operators - AND, OR, XOR, NOT
d = 5  # In binary: 0101
e = 3  # In binary: 0011
print(d & e)  # Output: 1 (In binary: 0001)
