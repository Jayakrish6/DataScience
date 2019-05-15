# -*- coding: utf-8 -*-
import calendar

cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)

sum = lambda arg1, arg2: arg1 + arg2;

# Now you can call sum as a function
print ("Value of total : ", sum( 10, 20 ))
print ("Value of total : ", sum( 20, 20 ))
