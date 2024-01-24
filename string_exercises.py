# QUESTION 1: Take an input string from the user and create a new string
# with the first, middle, and last characters of the input string
# 1. Take the user input and set it to a variable
user_string = input('Please enter a string: ')
print(user_string)

# 2.Get the first character using index 0 and store it in a variable
first_char = user_string[0]
last_char = user_string[-1]

str_length = len(user_string)
mid_index = int(str_length/2) # need to convert to int because indices should always be integers
print(mid_index)

mid_char = user_string[mid_index]

new_str = first_char+mid_char+last_char
print(new_str)













user_string = input('Please enter a string: ')
print(user_string)

first_char = user_string[0]
last_char = user_string[-1]

# To get the middle character, find length and index of middle character
str_length = len(user_string)
mid_index = int(str_length/2) # since indices can only be integers

mid_char = user_string[mid_index] # To access the char at mid index
result_str = first_char + mid_char + last_char
print(result_str)