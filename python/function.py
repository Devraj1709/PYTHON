# 1. simple greeting function
def greet():
    print("Hello Everyone")
greet()

# 2. function with parameters
def show_name(name):
    print("My name is", name)
show_name("devraj")

# 3. addition function
def add(a, b):
    print("The sum is", a + b)
add(5, 3)

# 4. function with return value
def multiply(x, y):
    return x * y
result = multiply(4, 6)
print("The product is", result)

# 5. function to concatenate text
def join_text(text1, text2):
    return text1 + " " + text2

concatenated = join_text("Hello", "World")
print(concatenated)
