my_name = "devraj"
# index =  0 1 2 3 4 5
# index = -6 -5 -4 -3 -2 -1
# String slicing and indexing

print(my_name[0])  # Accessing the first character
print(my_name[1])  # Accessing the second character
print(my_name[2])  # Accessing the third character
print(my_name[-1])  # Accessing the last character
print(my_name[-2])  # Accessing the second last character
print(my_name[0:3])  # Accessing characters from index 0 to 2
print(my_name[3:])  # Accessing characters from index 3 to the end
print(my_name[:3])  # Accessing characters from the beginning to index 2
print(my_name[::2])  # Accessing every second character

word = "Rapper"
print(len(word))  # Length of the string
print(word.upper())  # Convert to uppercase
print(word.lower())  # Convert to lowercase
print(word.count('p'))  # Count occurrences of 'p'
print(word.find('p'))  # Find the index of the first occurrence of 'p'
print(word.split('p'))  # Split the string at 'p'
print(word.replace('p', 'b'))  # Replace 'p' with 'b'
print(word.title())  # Convert to title case

text = "   Hello, World!   "
print(text.strip())  # Remove leading and trailing whitespace

Z = "Python is great!"
print(Z)  # Print the string
print("-".join(Z))  # Join characters with a hyphen
