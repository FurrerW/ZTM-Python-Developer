# user_info = {
#     "first_name": "Walter",
#     "last_name": "Furrer",
#     "age": 32,
#     "country": "USA",
#     "state": "NY",
#     "city": "Islip",
# }

# city_state = user_info["city"] + ", " + user_info["state"]
# full_name = user_info["first_name"] + " " + user_info["last_name"]

# greeting = "Hi, my name is " + full_name + ". I am " + str(user_info["age"]) + " years old, and I live in " + city_state + "."

# print(greeting)

# greeting2 = f"Hi, my name is {full_name}."

# print(greeting2)

# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# iq = 100
# user_age = iq / 5 # Entire line of code is known as a statement.
# The value is known as the expression. AKA anything afer the =

#augmented assignment operator
# some_value = 5
# # some_value = 5 + 2
# some_value %= 2

# print(some_value)

# Type Conversion

# print(str(100))
# print(type(str(100)))
# print(100)
# print(type(100))

# Escape Sequences

# weather = 'It\'s sunny.'
# print(weather)

# weather2 = "\t \t It\'s \"kind of\" sunny. \n Hope you have a good day!"
# print(weather2)

#formatted strings

# name = 'Walter'
# age = 32

# print('Hi ' + name + '! You are ' + str(age) + ' years old.')
# print(f'Hi {name}! You are {age} years old.')

#Immutability: Strings in Python are IMMUTABLE - They cannot be changed

# selfish = '01234567'

# selfish[0] = '8' This does not work as strings are immutable. Can only completely remove the value '01234567' with something new

# selfish = selfish + 8 would print '12345678'

#Built-in Functions and Methods 
# https://docs.python.org/3/library/functions.html

# print(len('helloooooooooo')) # The length of the string is 14 characters long. len() does not start at 0, it starts at 1

# greet = "helloooooooooo"
# print(greet[:])
# print(greet[0:len(greet)]) # = print(greet[0:14])

#Python String Methods - Usually have a .method in front of them (.format, for example)
# https://www.w3schools.com/python/python_ref_string.asp

# quote = "to be or not to be..."

# quote.upper()
# print(quote)
# print(quote.upper())
# print(quote.capitalize())
# print(quote.title())
# print(quote.find("be"))
# print(quote.replace("be", "me"))

# print(quote)

#booleans - only true or false. 1 or 0. on or off.

# name = "Walter"
# is_cool = False

# is_cool = True

# if is_cool == True:
#     print(f"{name} is cool.")
# else:
#     print(f"{name} is not cool.")

# bool(1)
# print(bool(1))

# bool(0)
# print(bool(0))

# Lists

# li = ['a', 'b', 'c']
# print(li[0], li[1])

# Data Structure - Way for us to organize information and data into a folder/cupboard/box, so that they can be used with different pros/cons.

# amazon_cart = ["Notebooks", "Sunglasses"]

# for item in amazon_cart:
#     print(f"Alexa, add {item} to my shopping cart.")

# List Slicing

# amazon_cart = [
#     "Notebooks",
#     "Sunglasses",
#     "Toys",
#     "Grapes"
# ]

# amazon_cart[0] = "Laptop"
# new_cart = amazon_cart[:]
# new_cart[0] = "gum"
# print(new_cart)
# print(amazon_cart)

# Strings are immutable, right? They can't be changed.
# Lists are mutable. 



