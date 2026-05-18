# dictionary in python
# method 1: create dictionary curl braces 
Cohort = {
    "course": "Python",
    "duration": "3 months",
    "level": "beginner"
}
print(type(Cohort)) # <class 'dict'>
print(Cohort) # {'course': 'Python', 'duration': '3 months', 'level': 'beginner'}

# method 2: using dict() constructor
person = dict(name="devraj", age=18, grade="A")
print(type(person)) # <class 'dict'>
print(person) # {'name': 'devraj', 'age': 18, 'grade': 'A'}

# method 3: using list of tuples
person = dict([("name", "devraj"), ("age", 18), ("city", "Haryana")])
print(type(person)) # <class 'dict'>
print(person) # {'name': 'devraj', 'age': 18, 'city': 'Haryana'}

# acess dictionary values
student = {
    1: "class 12th",
    "name": "devraj",
    "grade": "A",
    "city": "Haryana"
}
print(student[1]) # class 12th
print(student["name"]) # devraj
print(student["grade"]) # A
print(student["city"]) # Haryana
# keys, values, items
print(student.keys()) # dict_keys([1, 'name', 'grade', 'city'])
print(student.values()) # dict_values(['class 12th', 'devraj', 'A', 'Haryana'])
print(student.items()) # dict_items([(1, 'class 12th'), ('name', 'devraj'), ('grade', 'A'), ('city', 'Haryana')])
# get method
print(student.get("name")) # devraj
print(student.get("age", "Not found")) # Not found

# add item-assign operator
student["email"] = "devraj123@gmail.com"
print(student) # {1: 'class 12th', 'name': 'devraj', 'grade': 'A', 'city': 'Haryana', 'email': 'devraj123@gmail.com'}
print(student["email"]) # devraj123@gmail.com

# modify/replace item-assign operator
student["grade"] = "A+"
print(student) # {1: 'class 12th', 'name': 'devraj', 'grade': 'A+', 'city': 'Haryana', 'email': 'devraj123@gmail.com'}
print(student["grade"]) # A+

# delete item using del statement
del student["email"]
print(student) # {1: 'class 12th', 'name': 'devraj', 'grade': 'A+', 'city': 'Haryana'}
student.pop("city")
print(student) # {1: 'class 12th', 'name': 'devraj', 'grade': 'A+'}

# dictionary Iterations
student = {
    "name": "devraj",
    "grade": "A+",
    "city": "Haryana"
}

# loop through keys
for keys in student:
    print(keys) # name, grade, city
    
# for loop through values
for values in student.values():
    print(values) # devraj, A+, Haryana
    
# nested dictionary
main_student = {
    "student1": {
        "name": "devraj",
        "age": 18},
    "student2": {
        "name": "shivam",
        "age": 19}
}
print(main_student) # {'student1': {'name': 'devraj', 'age': 18}, 'student2': {'name': 'shivam', 'age': 19}}
print(main_student["student1"]) # {'name': 'devraj', 'age': 18}
