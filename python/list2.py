# Reverse List
fruits = ["apple", "banana", "orange"]
fruits.reverse()
print(fruits) # ['orange', 'banana', 'apple']

# sorting with a key
words = ["banana", "apple", "grape", "kiwi"]
words.sort(key=len)
print(words) # ['kiwi', 'grape', 'apple', 'banana']

# 10pop with index value
numbers = [10, 20, 30, 40, 50]
popped = numbers.pop(2)
print(popped) # 30

# pop with default
last = numbers.pop()
print(last) # 50
print(numbers) # [10, 20, 40]

# 11 copying list
fruits = ["apple", "banana", "orange"]
copy_fruits = fruits.copy()
print(copy_fruits) # ['apple', 'banana', 'orange']

# Join Lists
list1 = [1, 2, 3]
list2 = ['a', 'b']
joined = list1 + list2
print(joined) # [1, 2, 3, 'a', 'b']
