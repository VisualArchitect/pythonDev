# This is my first python program that I wrote myself
# Updated on 07-05-2023

import math

first_name = "Ricardo"
last_name = "Sewell"
age = 36
birth_place = "Atlanta"
current_year = 2023
birth_year = current_year - age
places_traveled = ["Oceanside, Tokyo, Atanta, Princeton"]
employed = True

phrase = f"{first_name} {last_name} {'is'} {age} {'years old and born on'} {birth_year}"
print(phrase)

# This is the old way of concatenating strings with other variables
"""
print(
    first_name
    + " "
    + last_name
    + " is "
    + str(age)
    + " years old and born in "
    + str(birth_year)
)
"""
# This is an example of a method for Strings
print(last_name.upper())

# An expression is a piece of code that returns a value
print("Ric" in first_name)

# Number stuff

print(round(36.6))

# Getting user input in Python
user_response = input("x: ")
y = user_response + 1