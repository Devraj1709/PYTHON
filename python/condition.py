# Conditional statement in python

# if statement
# if statement works only for true condition
# a=10
# b=20
# if a<b:
#     print("a is less than b")

# age=18
# if age>=18:
#     print("you are an adult")
    
# if-else statement
# else statement works only for false condition
age=17
if age>18:
    print("you are an adult")
else:
    print("you are not an adult")

temp = 15
if temp > 10:
    print("it is a cold day")
else:
    print("it is a hot day")
    
marks = int(input("enter your marks: "))
if marks > 33:
    print("Pass")
else:
    print("Fail")
    
# check whether a number is even or odd
num = int(input("enter a number: "))
if num % 2 == 0:
    print("even") 
else:
    print("odd")