my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))

my_list2 = [1, 'devraj', 'shivam', True, 3.14]
print(my_list2)

my_list3 = [1, 2,[3,4], True, [5,6,7]]
print(my_list3)

# Access List-indexing
list1 = [10, 20, 30, 40, 50]
print(list1[0]) # 10
print(list1[2]) # 30
print(list1[4]) # 50

fruits = ["apple", "banana", "orange"]
fruits.append("cherry")
print(fruits) # ['apple', 'banana', 'orange', 'cherry']

#extend
fruits1 = ["grape", "melon"]
more_fruits = ["kiwi", "date"]
fruits1.extend(more_fruits)
print(fruits1) # ['grape', 'melon', 'kiwi', 'date']

#insert
fruits2 = ["pear", "plum"]
fruits2.insert(1, "mango")
print(fruits2) # ['pear', 'mango', 'plum']

#remove
fruits3 = ["strawberry", "blueberry", "raspberry"]
fruits3.remove("blueberry")
print(fruits3) # ['strawberry', 'raspberry']

#clear
fruits4 = ["watermelon", "papaya", "pineapple"]
fruits4.clear()
print(fruits4) # []

# finding index
fruits5 = ["apple", "banana", "orange"]
index = fruits5.index("banana")
print(index) # 1

#sorting list
numbers = [5, 2, 9, 1, 5]
numbers.sort()
print(numbers) # [1, 2, 5, 5, 9]

#sorthing in descending order
numbers2 = [5, 2, 9, 1, 5]
numbers2.sort(reverse=True)
print(numbers2) # [9, 5, 5, 2, 1]
