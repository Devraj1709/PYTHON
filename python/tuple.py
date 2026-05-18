# Tuple in Python

my_tuple = (1, 2, 3, 4, 5)
print(my_tuple) # (1, 2, 3, 4, 5
print(type(my_tuple)) # <class 'tuple'>

# create tuples
# 1. using parentheses
tuple1 = (1, 2, 3)
print(tuple1) # (1, 2, 3)
print(type(tuple1)) # <class 'tuple'>

# 2. without parentheses
tuple2 = 4, 5, 6
print(tuple2) # (4, 5, 6)
print(type(tuple2)) # <class 'tuple'>

# 3. tuple constructor
tuple3 = tuple([7, 8, 9])
print(tuple3) # (7, 8, 9)
print(type(tuple3)) # <class 'tuple'>

list1 = [10, 11, 12]
tuple4 = tuple(list1)
print(tuple4) # (10, 11, 12)
print(type(tuple4)) # <class 'tuple'>

# create a single element 
single_tuple = (42,)
print(single_tuple) # (42,)
print(type(single_tuple)) # <class 'tuple'>

# access tuple-indexing
fruits = ("apple", "banana", "orange")
print(fruits[0]) # apple
print(fruits[1]) # banana
print(fruits[2]) # orange

# tuple slicing
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4]) # (2, 3, 4)
print(numbers[:3]) # (1, 2, 3)
print(numbers[2:5]) # (3, 4, 5)
print(numbers[0:5]) # (1, 2, 3, 4, 5)

# concatenate-join tuples
tuple_a = (1, 2, 3)
tuple_b = (4, 5, 6)
joined_tuple = tuple_a + tuple_b
print(joined_tuple) # (1, 2, 3, 4, 5, 6)

# repeatitive tuples
tuple_c = (7, 8)
repeated_tuple = tuple_c * 3
print(repeated_tuple) # (7, 8, 7, 8, 7, 8)

# checking a element in a tuple
fruits = ("apple", "banana", "orange")
print("banana" in fruits) # True
print("grape" in fruits) # False

# tuple iteration
# for loop
fruits = ("apple", "banana", "orange")
for i in fruits:
    print(i)

# while loop
numbers = (1, 2, 3, 4, 5)
i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1
    
# tuple methods
colors = ("red", "green", "blue", "red")
# count method
print(colors.count("red")) # 2
print(colors.count("green")) # 1
print(colors.count("yellow")) # 0

# index method
print(colors.index("blue")) # 2
print(colors.index("red")) # 0 (first occurrence)

