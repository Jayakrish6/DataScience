# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
from numpy.random import randn

labels = ['a', 'b', 'c']
myData = [10, 20, 30]
arr = np.array(myData)
d = {'a':10, 'b':20, 'c':30}

print(pd.Series(data = myData, index=labels))

print(pd.Series(d))

print(pd.Series(data = [sum, print, len]))

ser1 = pd.Series([1,2,3,4], ['USA', 'GERMANY', 'USSR', 'Japan'])
print(ser1)
ser2 = pd.Series([1,2,5,4], ['USA', 'GERMANY', 'Italy', 'Japan'])
print(ser2)

print(ser1 + ser2)

#--------------------------------------------------------
#---------------DATAFRAME -------------------------------
#--------------------------------------------------------

np.random.seed(101)
df = pd.DataFrame(randn(5,4), ['A', 'B', 'C', 'D', 'E'], ['W', 'X', 'Y', 'Z'])
print(type(df['W']))
print(df.W)

print(df.reset_index())
print(df[df['W']>0][['Y','X']])

boolSer = df['W'] > 0
result = df[boolSer]
myCol = ['Y', 'X']
print(result[myCol])

print(df.reset_index())
newInd = 'CA NY WY OR CO'.split()
df['States'] = newInd
print(df)
print(df.set_index('States'))
