# set using curly braces
my_set = {1, 2, 3, 4, 5}
print(type(my_set)) # <class 'set'>

# creating using setconstructor
my_set = set([1, 2, 3, 4, 5])
print(type(my_set)) # <class 'set'>
print(my_set) # {1, 2, 3, 4, 5}

# set operations
# adding elements
numbers = {1, 2, 3}
numbers.add(4)
print(numbers) # {1, 2, 3, 4}

# removing elements
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits) # {"apple", "cherry"}

# discard
fruits.discard("grape") # does not show error
print(fruits) # {"apple", "cherry"}

# set methods
# 1. union-combines elements of two sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set) # {1, 2, 3, 4, 5}

# union alternative
union_set = set1 | set2
print(union_set) # {1, 2, 3, 4, 5}

# 2. intersection-returns common elements
intersection_set = set1.intersection(set2)
print(intersection_set) # {3}

# intersection alternative
intersection_set = set1 & set2
print(intersection_set) # {3}

# 3. difference-returns elements present in first set only
# but not in second set
difference_set = set1.difference(set2)
print(difference_set) # {1, 2}

# difference alternative
difference_set = set1 - set2
print(difference_set) # {1, 2}

# 4. symmetric difference-returns elements in either set but not in both
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set) # {1, 2, 4, 5}

# symmetric difference alternative
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set) # {1, 2, 4, 5}

# set iterations
my_set = {1, 2, 3, 4, 5}
for i in my_set:
    print(i) # 1, 2, 3, 4, 5
    
# while loop doesn't support
# for i in my_set:
#     print(i)
    
# set comprehensions
squared_set = {x**2 for x in range(1, 6)}
print(squared_set) # {1, 4, 9, 16, 25}
