name = input("Enter your name: ")

a1 = input("Enter marks in subject 1: ")
a2 = input("Enter marks in subject 2: ")
a3 = input("Enter marks in subject 3: ")
a4 = input("Enter marks in subject 4: ")
a5 = input("Enter marks in subject 5: ")
total = int(a1) + int(a2) + int(a3) + int(a4) + int(a5)
percentage = (total / 500) * 100
print("Total marks: " + str(total))

print("Name: ", name)
print("Total:", total)
print("percentage:", percentage)