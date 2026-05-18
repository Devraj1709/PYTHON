# loops in python-while & for loop

# while loop
i = 1
while i < 5:
    print(i)
    i += 1
    
# print numbers from 1 to 10 using while loop
j = 1
while j < 10:
    print(j)
    j += 1
    
k = 1
while k > 0:
    print(k)
    k -= 1
    
else:
    print("Loop has ended")

# for loop
languages = ["Python", "Java", "C++", "JavaScript"]
for language in languages:
    print(language)
    
# range(start, stop, step)
for i in range(0, 10, 2):
    print(i)
    
for j in range(5):
    print(j)
    
for k in range(1, 11):
    print(k)
    
else:
    print("For loop has ended")

