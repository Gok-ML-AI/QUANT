# Pandas Series
"""
A Pandas series is basically what you get if
"A Dictionary and Numpy 1D Array Had a Baby"
Think of it as having all the efficient, mathematical & statistical operations  embedded in a Numpy 1 Dimensional array
While maintaining some key value mapping construction present in a dictionary.
1. Construction & Deconstruction
2. Retrieving values
3. Modify Values
4. Methods for Data Analysis
5. Data Alignment
"""

# Imports
import pandas as pd
import numpy as np

# Series Construction
# Series construction w/ dict - representing the returns within a particular day with ticker symbols
ret_dict = {'AAPL':-0.01, 'MSFT':-0.02, 'TSLA':0.015, 'LULU':-0.005}
ser=pd.Series(ret_dict)
print("The series (with dictionary) : ", ser)
print()

# Series construction w/ two lists
ret = [-0.01, -0.02, 0.015, -0.005]
tickers = ['AAPL', 'MSFT', 'TSLA', 'LULU']
ser = pd.Series(ret, index=tickers)
print("The Series (with 2 lists) : ", ser)
print()

# Series construction w/ list without keys
ser = pd.Series([-0.01, -0.02, 0.015, -0.005])
print("The Series (without keys) : ", ser)
print()

# Series Construction
ser= pd.Series({'AAPL':-0.01, 'MSFT':-0.02, 'TSLA':0.015, 'LULU':-0.005})
print("ser : ", ser)
print("ser.values : ", ser.values)
print("ser.index : ", ser.index)
print()


# Retrieve & Modify
# Retrieving Values from Series

ret_dict = {'AAPL':-0.01, 'MSFT':-0.02, 'TSLA':0.015, 'LULU':-0.005}
print()
ser = pd.Series(ret_dict)
# retrieval using key
print("Retrieving 'MSFT' values from the series : ", ser['MSFT'])
print()

# retrieval using integers
print("Retrieving using integers ser.iloc[1] : ", ser.iloc[1])
print()

# Multi Item Retrieval
print("Multi Item Retrieval using 'keys' - ser[['AAPL', 'TSLA']] : ", ser[['AAPL', 'TSLA']])
print()

# Multi Item Integer Retrieval using Integers
print("Multi Item Integer Retrieval using Integers ser.iloc[[0,2]] : ", ser.iloc[[0,2]])
print()

# Multi Item Slicing
index = ['20201201', '20201202', '20201203', '20201204']
tser = pd.Series([-0.01, 0.015,-0.025,-0.03], index=index)
print("Multi Item 'Slicing' - tser : ", tser)
print()

# Slicing using keys
print("Slicing using keys - tser['20201202': '20201204'] : ", tser['20201202': '20201204'])
print()

# slicing using integers
print("Slicing using integers tser.iloc[0:3] : ", tser.iloc[0:3])
print()

# get only +ve values using 'boolean' indexing
# 1st create a boolean mask called 'filt'
# Then pass 'filt' into the series to get the +ve values
filt = ser > 0
print("Get boolean mask of values in 'ser'  : ", filt)
print()

print("Get only +ve values from 'ser' : ", ser[filt])
print()

# get only -ve values
print("Geting only -ve inputs from 'ser' : ", ser[ser<0])
print()

# Get only return > 5%
print("Get only return > 5% : ", ser[ser>0.05])
print()


# Modifying Values in Series
print("Get 'AAPL' from 'ser' before changing value : ", ser['AAPL'])
ser['AAPL']=-0.02
print("Get 'AAPL' from 'ser' AFTER changing value : ", ser['AAPL'])
print()

# Changing Multiple values
print("Get 'AAPL' and  'TSLA' from 'ser' BEFORE changing value : ", ser[['AAPL',  'TSLA']])
print()
print("Modifying Multiple values in 'ser' - ser[['AAPL', 'TSLA']]= [-0.03, 0.03] ")
ser[['AAPL', 'TSLA']]= [-0.03, 0.03]
print()
print("Get 'AAPL' and  'TSLA' from 'ser' AFTER changing value : ", ser[['AAPL',  'TSLA']])
print()

# Modifying any values using boolean indexing where 'value < 0' and changing to '0'
print("Getting 'ser' values before update any less than 0 to 0 : ", ser)
print()
print("Changing values of 'ser' using boolean indexing - ser[ser<0]=0 .")
print()
ser[ser<0]=0
print("Getting 'ser' values after update any less than 0 to 0 : ", ser)
print()

# Modifying values by Slicing method above
ser[['AAPL', 'MSFT', 'TSLA', 'LULU']]=-0.02
print("Getting 'ser' values before update 'MSFT' TO 'LULU' : ", ser)
print()
ser['MSFT':'LULU']=0
print("Getting 'ser' values after update 'MSFT' TO 'LULU' : ", ser)
print()

# Can also Modify the Index of a Series
ser[['AAPL', 'MSFT']]=-0.02
ser[['TSLA', 'LULU']]=-0.04
print("Getting 'ser' values before update index : ", ser)
ser.index=['TSLA', 'MSFT', 'AAPL', 'GOOGL']
print("Getting 'ser' values AFTER update index : ", ser)
print()
print()

# Series Methods for Data Analysis
"""
1. Arithmetic & boolean operations with scalars operates element wise
2. Numpy universal functions operate element-wise as they do with arrays
3. Series map - apply any function element-wise
4. Series have many built in methods similar to numpy arrays
"""

# Arithmetic & Boolean operations
# series construction w/ dict
import pandas as pd

ret_dict = {'AAPL':-0.01, 'MSFT':-0.02, 'TSLA': 0.015, 'LULU':-0.005}
ser = pd.Series(ret_dict)
print("Series initialisation : ", ser)

# Scalar arithmetic is much easier with a series
mkt_ret = 0.005
print("The Series after subtracting the Market return : ", ser - mkt_ret)

# Scalar arithmetic is very hard with a dict... need to use a loop
mkt_ret = 0.005
ret_dict = {'AAPL':-0.01, 'MSFT':-0.02, 'TSLA': 0.015}
print("The current value of ret_dict : ", ret_dict)
print()

dict_excess={}
for key in ret_dict:
    dict_excess[key] = ret_dict[key]-mkt_ret
print("After looping through ret_dict and subtracting mkt_ret : ", dict_excess)
print()
# Scalar arithmetic is much easier with a series
mkt_ret = 0.005
ser - mkt_ret
print("Ser values : ", ser)
print()

# boolean logic operates element-wise
print("SER is > 0 : ", ser > 0)
print()

# get sign of returns
print("Print the sign values of Series :  ",np.sign(ser))
print()

# Series  map - apply any function element-wise

# Map
def thresh(x):
    if x > mkt_ret:
        return x
    else:
        return mkt_ret

print("The values before applying Thresh function : ", ser)
print()
print("Applying the thresh() function to the series")
print("Will return the mkt_ret if series value is less than mkt_ret.")
print(ser.map(thresh))
print()

# Might be easier to use lambda syntactic sugar
# Also can be achieved by
print("Using Lambda to apply thresh logic : ", ser.map(lambda x: x if x > mkt_ret else mkt_ret))
print()

# Series have various built in methods similar to numpy arrays

# Average Return
print("Ser Average Return : ", ser.mean())
print()

# Min Return
print("Ser Min Return : ", ser.min())
print()

# Standard Deviation
print("Ser Standard Deviation : ", ser.std())
print()

# Do NOT do this for the average
# When ever you find yourself writing a loop, check if there is a better way

avg = 0
for x in ser.values:
    avg+=x
avg=avg/len(ser)
print("The average of Series values using a loop : ", avg)
print()

# Return the ascending order rank of items
print("The ascending order of the Series : ", ser.rank())
print()

#
print("returning summary stats on the original series : ", ser.describe())
print()

# Alignment
# Series Data Alignment
# 1. Arithmetic Alignment
# 2. Boolean Alignment

import pandas as pd

print("The returns on 2 different days for tickers :")

ret1 = pd.Series({"VXX":0.01, 'AAPL':0.01, 'LULU':-0.01, 'TSLA':-0.03, 'MSFT':-0.01})
print("The initialized day1 returns : ", ret1)
print()

ret2 = pd.Series({'VXX':0.02, 'AAPL':-0.01, 'LULU':0.02, 'TSLA':-0.04, 'MSFT':-0.02})
print("The initialized day2 returns : ", ret2)
print()


print("Adding the 2 days returns -> 'ret2 + ret1' : ", ret2 + ret1)
print()

#
ret3 = pd.Series({'TSLA':-0.01, 'AAPL':0.02})
print("The initialized day 3 returns : ", ret3)
print()

#

print("Adding the 2 days returns when not all matching tickers -> 'ret1 + ret3' : ", ret1 + ret3)
print()

# can be done with div(), sub(), mul() etc.
print("Fill values with Nan to keep original values in original series : ", ret1.add(ret3, fill_value=0))
print()

# Boolean Alignment

#
print("Is the element in ret1 > than the element in ret3 (return new series : ", ret1 > ret2)
print()

# This will not work as can only compare identically labeled series
# print(" : ", ret1 > ret3)
# print()



bool1 = (ret1 > 0)
print("Create a new boolean series and check if ret1 > 0 : ", bool1)
print()

#
bool2 = (ret2 > 0)
print("Create a new boolean series and check if ret2 > 0 : ", bool2)
print()

#
print("The value of bool1 : ", bool1)
print()

print("The value of bool2 : ", bool2)
print()

print("bool1 & bool2 : ", bool1 & bool2)
print()

print("bool1 | bool2 : ", bool1 | bool2)
print()

print("Will do Series alignment when doing comparison.")
print("bool2 & bool1[['MSFT', 'TSLA', 'LULU', 'AAPL', 'VXX']] : ", bool2 & bool1[['MSFT', 'TSLA', 'LULU', 'AAPL', 'VXX']])
print()

print("Will do Series alignment when doing comparison, if NOT present will assume value is false.")
print("bool2 & bool1[['MSFT', 'TSLA', 'LULU', 'AAPL', 'VXX']] : ", bool2 & bool1[['VXX']])
print()