# -*- coding: utf-8 -*-
import math 
from collections import Counter
#from matplotlib import pyplot as plt

num_friends = [100, 49, 41, 40, 25, 101, 213, 12, 32, 55]
daily_minutes = [23, 234, 54, 65, 76, 87, 976, 34, 12, 65]
num_points = len(num_friends)
largest_value = max(num_friends) # 100
smallest_value = min(num_friends)
print(num_points, largest_value, smallest_value)

sorted_values = sorted(num_friends)
smallest_value = sorted_values[0] # 1
second_smallest_value = sorted_values[1] # 1
second_largest_value = sorted_values[-7]
print(sorted_values, smallest_value, second_smallest_value, 
      second_largest_value)

# #Mean - this isn't right if you don't from __future__ import division
def mean(x):
    return sum(x) / len(x)
mean_value = mean(num_friends) # 7.333333
print("Mean: ", mean_value)

def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    print(n, midpoint, sorted_v)
    if n % 2 == 1:
    # if odd, return the middle value
        print("Insight if() block")
        return sorted_v[midpoint]
    else:
    # if even, return the average of the middle values
        print("Insight else() block")
        lo = midpoint - 1
        hi = midpoint
        print(lo, hi, sorted_v[lo], sorted_v[hi])
        return (sorted_v[lo] + sorted_v[hi]) / 2
print("Median: ", median(num_friends)) # 6.0

#====================================================

def quantile(x, p):
    """returns the pth-percentile value in x"""
    p_index = int(p * len(x))
    return sorted(x)[p_index]

print(quantile(num_friends, 0.10)) # 1
print(quantile(num_friends, 0.25)) # 3
print(quantile(num_friends, 0.75)) # 9
print(quantile(num_friends, 0.90)) # 13
print("===================================")
def mode(x):
    """returns a list, might be more than one mode"""
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in counts.items() 
            if count == max_count]
print("===================================")
   
print(mode(num_friends)) # 1 and 6


def data_range(x):
    return max(x) - min(x)
print("Data Range:",data_range(num_friends)) # 99
#====================================================================

def dot(v, w):
    """v_1 * w_1 + ... + v_n * w_n"""
    print("dot:")
    return sum(v_i * w_i 
               for v_i, w_i in zip(v, w))

def sum_of_squares(v):
    """v_1 * v_1 + ... + v_n * v_n"""
    print("Insight sum_of_squares")
    return dot(v, v)

def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    print("X-bar: ", x_bar)
    return [x_i - x_bar for x_i in x]

def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)
print("Variance:",variance(num_friends)) # 81.54

#====================================================================

def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)
print("Covariance: ",covariance(num_friends, daily_minutes)) # 22.43

def standard_deviation(x):
    return math.sqrt(variance(x))
print("Standard deviation: ",standard_deviation(num_friends)) # 9.03

def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0 # if no variation, correlation is zero
print("Correlation: ",correlation(num_friends, daily_minutes)) # 0.25


outlier = num_friends.index(100) # index of outlier
num_friends_good = [x
                    for i, x in enumerate(num_friends)
                    if i != outlier]
daily_minutes_good = [x
                        for i, x in enumerate(daily_minutes)
                        if i != outlier]
print("Correlation2: ",
      correlation(num_friends_good, daily_minutes_good)) # 0.57

#========================================================================