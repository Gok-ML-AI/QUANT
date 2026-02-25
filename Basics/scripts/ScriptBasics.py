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
print()

# STRINGs
# Assignment - can use single or double quotes
ticker = 'AAPL US EQUITY'
ticker2 = "AAPL US EQUITY"
print(ticker)
print(ticker2)
print()

# Again, python AUtomatically infers the type
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