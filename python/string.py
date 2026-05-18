print("Hello, World!")  # This is a string literal
print("Won't Give Up!")  # Using single quotes inside double quotes
print('''"wow" and 'you' are very smart''')  # Using triple quotes for mixed quotes

# 1. Old style string formatting using % operator
name = "devraj"
age = 18
print("My name is %s and I am %d years old." % (name, age))
# 2. New style string formatting using str.format()
print("My name is {} and I am {} years old.".format(name, age))
# 3. f-string 
print(f"My name is {name} and I am {age} years old.")

# Escape characters
print("hello\nworld")  # New line
print("hello\tworld")  # Tab

# String Operators in Python
a = "Hello"
b = "Python"

print(a+b)  # Concatenation
print(a*3)  # Repetition

# slice, [:] - range -- scroll below
if "H" in a:
    print("H is present in a")
else:
    print("H is not present in a")
    
print(r"Hello\nWorld")  # Raw string - ignores escape characters

# /n: New line - Breaks the string into a new line.
print("Hello, World!\nWelcome to Python programming.")
# /t: Tab - Inserts a tab space in the string.
print("Name:\tDevraj")
# /": Double Quote - Allows you to include double quotes in a string.
print("She said, \"Python is great!\"")
# /': Single Quote - Allows you to include single quotes in a string.
print('It\'s a beautiful day for coding!')
# \\: Backslash - Allows you to include a backslash in a string.
print("This is a backslash: \\")
# /b: Backspace - Removes the previous character in the string.
print("Hello, World!\bWelcome to Python programming.")
# /r: Carriage Return - Moves the cursor to the beginning of the line.
print("Hello, World!\rWelcome to Python programming.")
