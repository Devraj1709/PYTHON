# casting in python
a=1
print(type(a)) # int
b="1"
# print(a+b)
c=int(b)
print(a+c) 
print(a+int(b))
name = "devraj"
# newname = int(name) 

number = 37
number2 = str(number)
print(type(number), type(number2))

f1 = 17.5
f2 = int(f1)
print(f2)

dj = 21
dj2 = float(dj)
print(dj2)

# implicit type casting
arc = 10 # int
arc2 = 5.5 # float
arc3 = arc + arc2
print(arc3) # 15.5
print(type(arc3)) # float

#explicit type casting
int_num = 10
str_num = str(int_num)
print(str_num) # "10"
print(type(str_num)) # <class 'str'>

dst=bool(0) # False
print(dst) # False
print(type(dst)) # <class 'bool'>