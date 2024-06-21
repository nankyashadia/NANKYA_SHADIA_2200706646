# python best practices
"""Follow PEP 8
1: Indentation
2:Maximum line length
3:Blank lines
4: Use meaningful names
6:Use list comprehension"""
# Example of a meaningful name
# def calculate_area(radius):
# pass
# total_price= 10000

# Example of a lazy student bad meaningful name
# Example of a lazy student with bad meaningful name
# def calc(r):
# tp=1000


# python operators
"""_summary_#Addition
Name of the operator             Symbol with example
Addition                          x+y
#Subtraction                      x-y
#division                         x/y
#modulus                          x%y
# exponentiation                  x**y
Floor division                    x//y
"""


# Example of comparison operator
# Name of the operator              Symbol with example
# Equal                              x==y
# Not Equal                          x!=y
# Greater than                       x>y
# Less than                       x<y

# greater or equal                   x>=yy
# less or equal to                   x<=y
# and                                and
# or                                 or
# not                                not

"""# Example of membership operators

# in
# not in
# Example of python Bitwise operator
# Name          Symbol with example
# AND           &
# OR            |
# XOR           ~
# NOT          !
# pythoN cases
#  Name         symbol with example
# snake_case   
# camelCase
# UPPERCASE"""

# Comprehensions(List, dictionary
"""_summary_
 Comprehensions provides a
 concise way of create list and dictionary

Lists []brackets 
dictionary {} curly brackets

"""
# Example 1
# Basic list comprehension
# create a list of squares in a list of 10
list_of_squares=[x**2 for x in range (10)]
print(list_of_squares)
# Example 2:
# create a list of even squares in the range of 20

# 

list_of_even_squares=[x**2 for x in range(20) if (x %2==0)]

    
print(list_of_even_squares)
# dictionary comprehension
# create a dictionary comprehension for my favorite cars and count the length of the character
favorite_car=['BMW','Jeep','mercedes','fordraptor']
car_length={car:len(car) for car in favorite_car}
print(car_length)
# exercise
# Create a list of tuple where each tuple contains a number and its cube for numbers btn 1 and 10 using a dictionary comprehension 
list_of_tuple={x:x**3 for x in range(1,11)}
print(list_of_tuple)
               
    