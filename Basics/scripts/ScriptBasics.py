# Python Intro
"""
1. Variables
2. Basic data types (Numbers, strings, Booleans)
3. Lists
4. Dictionaries
5. Functions
6. If/Else statements
7. Loops
8. Some Syntactic Sugar
this site is also a helpful resource https://www.w3schools.com/python
"""

# VARIABLES
# Variable assignment using "="
aapl_ret = 0.01
market_ret = 0.02

# Print statements outputs variable values
print(f"Apple stock returns : ",aapl_ret)
print(f"Market stock returns : ", market_ret)

# Variables can be defined in terms of other variables
excess_ret = aapl_ret - market_ret
print(f"Excess stock returns are : ", excess_ret)

# DATA TYPES
# Numbers
# there 2 main numeric data types : Integers and Floats
num_int = 5
num_float = 2.5
# use type to get the datatype
# Notice Python automatically infers the data type - no need to declare it separately
print(f"The type of 'num_int' is : ", type(num_int))
print(f"The type of 'num_float' is : ", type(num_float))
#
x = 2
y = 8
print("The value of 'x' =  ", x)
print("The value of 'y' =  ", y)

add = x + y
print(" add = x + y  : ", add)
subtract = x - y
print("subtract = x - y : ", subtract)
multiply = x * y
print("multiply = x * y : ", multiply)
divide = x / y
print("divide = x / y : ", divide)
modulus = x % y
print("modulus = x % y ; ", modulus)
exponent = x ** y
print("exponent = x ** y : ", exponent)
floor_div = x // y
print("floor_div = x // y : ", floor_div)

# STRING