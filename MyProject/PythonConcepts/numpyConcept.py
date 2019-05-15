# -*- coding: utf-8 -*-
import numpy as np

#arr_2d = np.array([[5, 10, 15], [20,25,30], [35, 40,45]])

#print(arr_2d)
#print(arr_2d[:0,:2])

#TODO: Take a 5:10 array and retrive chunks of 4 elements at a time

arr_2d = np.arange(50).reshape(5,10)
print(arr_2d)
print("")
print(arr_2d[0:, 7:11])

arr = np.arange(10)
#arr[:]=1
print(arr-arr+5)

arr = np.arange(10, 51, 2)
print(np.ones(10)+4)
