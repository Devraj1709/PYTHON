# 1. if-elif-else condition multiple conditions
marks = int(input("Enter your marks out of 100: "))

if marks >= 90:
    print("Grade: A")
elif marks >= 80:
    print("Grade: B")
elif marks >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# 2. Example Traffic Light Signal
color = input("Enter the traffic light color: ")

if color == "red":
    print("Stop")
elif color == "yellow":
    print("Prepare to stop")
elif color == "green":
    print("Go")
else:
    print("Invalid color")
    
# 3. Nested if for more complex decision making
# Example : Login System
username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "admin":
    if password == "password123":
        print("Login successful!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")
    