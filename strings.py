# Strings in python are surrounded by either single or double quotation marks. 

name = 'Zsolt'
age = 35

# Concatenate

print('Hello, my name is ' + name + '. I am ' + str(age))

# String Formatting

# Arguments by position
print('Hello, my name is {name}. I am {age}'.format(name=name, age=age))

# F-Strings (3.6+)
print(f'Hello, my name is {name}. I am {age}')

# String Methods
s = 'hello world'

# Capitalize string
print(s.capitalize())

# Make all uppercase
print(s.upper())

# Make all lower
print(s.lower())

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))


# Count
print(s.count(s, 0, 5))

# Starts with
print(s.startswith('hello'))

# Ends with
print(s.endswith('rld'))

# Split into a list
print(s.split())

# Find position
print(s.find('w'))

# Is all alphanumeric - false because the space
print(s.isalnum())

# Is all alphabetic - false because the space
print(s.isalpha())

# Is all numeric
print(s.isnumeric())