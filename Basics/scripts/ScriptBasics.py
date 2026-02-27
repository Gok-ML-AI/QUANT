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
print()
print("*************************VARIABLES*************************")
print()
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
print()
print("*************************NUMBERS*************************")
print()
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
print()

# STRINGs
# Assignment - can use single or double quotes
print()
print("*************************STRINGS*************************")
print()
ticker = 'AAPL US EQUITY'
ticker2 = "AAPL US EQUITY"
print(ticker)
print(ticker2)
print()

# Again, python Automatically infers the type
print("The type of 'ticker' single quotes : ", type(ticker))
print("The type of 'ticker2' double quotes : ", type(ticker2))

# A string is an array: individual characters can be retrieved
dt = '20110501'
print()
print("The DateTime string : ", dt)
# Millennium
print("The output of 'dt[0]' is : ", dt[0])
# Year
print("The output of 'dt[0:4]' is Year : ", dt[0:4])
print("The output of 'dt[:4]' is Year : ", dt[:4])
# Month
print("The output of 'dt[4:6]' is Month : ", dt[4:6])
# Day
print("The output of 'dt[6:9]' is Day : ", dt[6:9])


# String is an array: can loop through a string
print()
print("A string is an array lets loop through the Dt string.")
print()
pos = 0
for x in dt:
    print(f"The value of 'x' at position {pos} is : {x}")
    pos+=1

# String Contains
print("Is 'Equity' in the 'ticker' string : ", 'Equity' in ticker)
print("Is 'JP Equity' in the 'ticker' string : ", 'JP Equity' in ticker)
print()

# Strings have many useful methods
print()
print("converting the 'ticker' string to all uppercase : ", ticker.upper())
print("converting the 'ticker' string to all lowercase : ", ticker.lower())

#
print()
ticker = 'AAPL US Equity   '
print(ticker)

# Strip out the whitespace
print()
print(f"The string 'ticker' : '{ticker}'  before being stripped of whitespace", ticker)
ticker = ticker.strip(' ')
print(f"The string 'ticker' : '{ticker}'  after being stripped of whitespace", ticker)

# Replace part of a String with Another String
print()
print(f"The string 'ticker' : '{ticker}'  before replacing some text with new text", ticker)
ticker = ticker.replace('US Equity', 'JP Equity')
print(f"The string 'ticker' : '{ticker}'  after replacing some text with new text", ticker)

# Split Up a String
tick_split = ticker.split(' ')
print("The 'ticker' string after splitting it into other strings using the space between each word : ", tick_split)
print()
print(tick_split)
print("The value of 'tick_slit[0]' : ", tick_split[0])
print("The value of 'tick_slit[1]' : ", tick_split[1])
print("The value of 'tick_slit[2]' : ", tick_split[2])

# Joining up a string in different ways
print()
print("'tick_split' joined up using empty space ' ' : ", ' '.join(tick_split))
print("'tick_split' joined up using star '*' : ", '*'.join(tick_split))
print("'tick_split' joined up using hyphon '-' : ", '-'.join(tick_split))

# Concatenation
print()
symbol = 'AAPL'
print("The 'symbol' string is: ", symbol)
country = 'US'
print("The 'country' string is: ", country)
asset = 'Equity'
print("The 'asset' string is: ", asset)
ticker_assembled = symbol + ' ' + country + ' ' + asset
print("The ticker_assembled is: ", ticker_assembled)

# Formatting
print()
print("Formatting the strings 'symbol', 'country', 'asset' gives me : '{} {} {}' ".format(symbol, country, asset))
# Formatting with Numbers
print()
print('Daily return of {} {} {} = {} pct'.format(symbol, country, asset, 1.55))
# Old way
print()
print("The Old Way to do this was")
print("Daily return of %s %s %s = %s pct"%(symbol, country, asset, 1.55))

# Tab completion string. 'tab' -> isupper(0, islower() etc.....
print()
print("There are lots and lots of string methods  using ticker.  'tab' .")
print()

# BOOLEANS
# Booleans are True or False Flags
# Used in loops & if/Else statements
# Used for indexing arrays etc...
print()
print("*************************BOOLEANS*************************")
print()

a = True
b = False
print(a)
print(b)

#
print()
print("The type of 'a' is : ", type(a))
print("The type of 'b' is : ", type(b))

# Generating booleans using operators on numbers
print()
x = 2
y = 3
print("x==y : ", x==y)
print("x!=y : ", x!=y)
print("x>y : ", x>y)
print("x < y : ", x<y)
print("x>=y : ", x>=y)
print("x<=y : ", x<=y)

# Generating booleans using operators on strings
print()
x = 'TSLA US Equity'
y = 'AAPL US Equity'
print("The string 'TSLA' is in x : ", 'TSLA' in x)
print("The string x==y : ", x==y)
print("The string x!=y : ", x!=y)

# Logical Operators
print()
x = 3
print("The value of x is : ", x)
print("x<10 and x>5 : ", x<10 and x>5)
print("not(x<10 and x>5) : ", not(x<10 and x>5))
print("x<10 or x>5 :", x<10 or x>5)

# Lists
print()
print("*************************LISTS*************************")
print()
# Create a list using square brackets
print()
stocks = ['AAPL', 'BAC', 'XOM', 'LULU']
print("The contents of 'stocks' list : ", stocks)
print("The type of 'stocks' is : ", type(stocks))

# lists can be of any data type
returns = [0.01, -0.01, 0.02, 0.03]
print()
print("The contents of the 'returns' list : ", returns)
print("The type of the 'returns' list : ", type(returns))

# Retrieving values
# Positive indexing
print()
print("The value of the stocks at position 0 by 'stocks[0]' : ", stocks[0])
print("The value of the stocks at position 2 by 'stocks[2]' : ", stocks[2])
print("The value of the stocks at position 3 by 'stocks[3]' : ", stocks[3])

# Negative indexing
print()
print("The value of the stocks at -ve position -1 by 'stocks[-1]' : ", stocks[-1])
print("The value of the stocks at -ve position -2 by 'stocks[-2]' : ", stocks[-2])
print("The value of the stocks at -ve position -4 by 'stocks[-4]' : ", stocks[-4])

# Index range w/ Positives
print()
print("The value of the stocks from range 1 to 3 'stocks[1:3]' : ", stocks[1:3])
print("The value of the stocks up to range  4 'stocks[:4]' : ", stocks[:4])
print("The value of the stocks from position 2 onwards 'stocks[2:]' : ", stocks[2:])

# Index range w/ Negatives
print()
print("The value of the stocks from -ve range -3 to -1 'stocks[-3:-1]' : ", stocks[-3:-1])
print("The value of the stocks from -ve range  -3 'stocks[-3:]' : ", stocks[-3:])
print("The value of the stocks from -ve range -2 onwards 'stocks[-2:]' : ", stocks[:-2])

# Check if an item exists
print()
print("Check if 'TSLA' in stocks : ", 'TSLA' in stocks)

# Changing Values
print()
print("Replacing/Changing an item in the List")
print("Replaing the first item 'AAPL' with 'MSFT")
print("Before : ", stocks)
stocks[0] = 'MSFT'
print("After : ", stocks)
# Inserting
print("Inserting the 'AAPL' into the list at position 1 'stocks.insert(1, 'AAPL') ")
stocks.insert(1,'AAPL')
print(stocks)
print("Appending the 'TWTR' symbol onto the list!")
stocks.append('TWTR')
print(stocks)
print("Removing 'AAPL' from the list with stocks.remmove('AAPL') !")
stocks.remove('AAPL')
print(stocks)
# Popping 1 from the list
print("Using stocks.pop() ro remove the last element from the list")
stocks.pop()
print(stocks)
# Combining lists
tech = ['AAPL', 'MSFT', 'FB']
print("Creating a list : tech = ['AAPL', 'MSFT', 'FB'] ")
print(tech)
fin = ['BAC', 'JPM', 'GS']
print("creating a list : fin = ['BAC', 'JPM', 'GS'] ")
print(fin)
print("Combining the 2 lists with 'tech + fin' ")
both = tech + fin
print(both)
print()
print("Sorting the list")
both.sort()
print(both)
print()

print("Creating a new List - 'stocksNew ")
stocksNew = ['AAPL','BAC','XOM','LULU']
print("stocksNew = ", stocksNew)
print("printing element from the list at position '[-3:-1][1]' ")
print(stocksNew[-3:-1][1])
print()


# DICTIONARIES
print()
print("*************************DICTIONARIES*************************")
print()

# A Key value Pair Mapping
# Creating a Dictionary
returns = {'AAPL':0.01, 'XOM':-0.02, 'BAC':0.05}
print("Created dictionary 'returns' : ", returns)
print("Type of returns : ", type(returns))


# Note: keys are typically strings, dates or number values can be numbers, lists, strings, dictionaries, etc.
mixed_dict = {'a':'b', 1:'c', 'list':[12345], 'dict':{'key':'value'}}
print()
print("Created Mixed Dictionary")
print(mixed_dict)

# Accessing items
print()
print("Accessing the returns dictionary at the key 'XOM'")
print(returns['XOM'])
print()
print("Printing just the values from the 'returns' dictionary.")
print(returns.values())
print()
print("Printing just the keys from the 'returns' dictionary.")
print(returns.keys())

# Changing items
print()
print("Changing the Values of the 'AAPL' in the returns dictionary")
print("Before: ", returns)
returns['AAPL']=-0.01
print("After : ", returns)

# Adding tems
print()
print("Adding an item to the dictionary ")
returns['TWTR']=0.005
print("After : ", returns)

# Deleting an item
print()
print("deleting the item 'TWTR' from the list using pop('TWTR').")
returns.pop('TWTR')
print("After : ", returns)

# Updating the Dictionary
print()
print("Updating the returns dictionary with {'XOM':-0.03, 'BAC':0.04, 'V':0.015} ")
print("Before Update : ", returns)
returns.update({'XOM':-0.03, 'BAC':0.04, 'V':0.015})
print("After Update : ", returns)

# FUNCTIONS
# Create Functions using the def Keyword
# Function arguments are specified in () above
# return keyword specifies function output
print()
print("*************************FUNCTIONS*************************")
print()

def add_2(x):
    result = x + 2
    return result

print("add_2(0) returns : ", add_2(0))
print("add_2(4) returns : ", add_2(4))

# body of function should be indented with tab

# functions can have multiple arguments
print()
def multiply(x, y):
    result = x*y
    return result

print("multiply(2,2) returns : ", multiply(2,2))
print("multiply(5,3) returns : ", multiply(5,3))
print()

def divide(x, y):
    result = x/y
    return result
print("divide(2,2) returns : ", divide(2, 2))
print("divide(5,3) returns : ", divide(5, 3))
print("divide(3,5) returns : ", divide(3, 5))
print("divide(y=3,x=5) returns : ", divide(y=3, x=5))

# function arguments can have defaults
print()
def multiply_default(x, y=2):
    result = x*y
    return result

print("multiply_default(2) returns : ", multiply_default(2))
print("multiply_default(2, y=3) returns : ", multiply_default(2, y=3))

print()
def multiply_multi_default(x, y=2, z=1):
    result = x*y*z
    return result

print("multiply_multi_default(2) returns : ", multiply_multi_default(2))
print("multiply_multi_default(2, 3) returns : ", multiply_multi_default(2, 3))
print("multiply_multi_default(2, z=2) returns : ", multiply_multi_default(2, z=2))

# function arguments can be of many types
print()
def multi_arg(arr, label, idx):
    result = 'Item {} in {} is {}'.format(idx, label, arr[idx])
    return result

print("multi_arg(['XOM', 'GS', 'WMT'], 'tickers',1) returns : ", multi_arg(['XOM', 'GS', 'WMT'], 'tickers',1))

# IF/ELSE Statements
print()
print("*************************IF/ELSE Statements*************************")
print()

# Basic Syntax