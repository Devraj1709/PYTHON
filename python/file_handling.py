# file handling in python
# modes: r - read, w - write, a - append, x - create

# open file
file = open('example.txt', 'r')

# read file
content = file.read() # read entire file
print(content)
file.close() 

# read first line
file = open('example.txt', 'r')
first_line = file.readline()
print(first_line)
file.close() 

# list entire file
file = open('example.txt', 'r') 
lines = file.readlines() # read lines into a list
print(lines)
file.close() 

# w-mode write to a file
file = open('example.txt', 'w')
file.write("\n namste mam! aap kaise ho?") # write to file
file.close()

# append mode
file = open('example.txt', 'a')
file.write("\n namste mam! aap kaise ho?") # append to file
file.close()
