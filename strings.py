# Adding a comment in the remote repo
# Do not use reserved keywords for variable names
'''
print('Hello World')
print(help('keywords'))

# Try to avoid multiple variable declaration simultaneously
a = b = c = 10 # shortcut for below. works but not recommended
a = 10
b = 10
c = 10
print(a,b,c)

# Statement vs Expression
x = 47  # statement
y = x + 10  # expression


# TYPE CONVERSION --> to change the data type of a variable#
# Convert floats and numeric strings to int
print(int("20"))
print("30")

print(type(int("20")))
print(int(14.21))

# print(int("20.24")) # errors out because int expects only whole numbers inside quotes
print(int(float("20.24")))

## STRINGS ##
# 3 ways to create a string - using either single, double, triple quotes
first_name = 'Jane'
last_name = "Doe"
address = "10 Main St."

job = "Physician's Assistant" # recommended to use double quotes for strings

## STRING FUNCTIONS
# len() --> returns the number of characters in a string
print(len("Hello"))

# upper and lower --> convert the string to appropriate case
print("Hello".upper())

# String concatenation - adding up strings
first_name = "Jane"
last_name = "Doe"
print(first_name + ' ' + last_name)
age = 24
print(first_name + ' ' + last_name + ':' + str(age))

# String multiplication - can multiple a string with an int
print("hello"*3)

# Accessing string characters - a string is just a sequence of characters
name = "Jane Doe"
print(name[2])
# print(name[8]) # throws index out of bound error

# Retrieving the character at a given index
print(name.index('o')) # returns 6
print(name.index('e')) # returns the index of first occurrence
'''


###### STRING SLICING ####
emp_name ="Jane Doe"
print(emp_name[2:6])
print(emp_name[:4])
print(emp_name[2:])
print(emp_name[-4:-1])
print(emp_name[1:6:2])

print(emp_name.count('e'))

print(emp_name.find('Doe'))

emp_name = emp_name.replace('Jane', 'John')

# Membership Test
print('oh' in emp_name)

# String Formatting
student_name = "Alice"
score = 87

print(student_name + ': ' +str(score))
print("Name: {} Score: {}".format(student_name, score))
# f-strings
print(f'Name: {student_name} Score: {score}')
print(f'10 times 3 is {10*3}')





