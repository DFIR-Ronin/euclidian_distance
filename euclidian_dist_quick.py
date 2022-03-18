# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math as math

# Eucladian Distance of two lists/arrays
list1 = [0.819, -0.329, 0.248, -0.677, 0.643, 0.825, 
         0.896, -0.595, 0.619, 0.135, 0.497, 0.744, 1.117]

list2 = [-1.023, -0.480, 0.049, 0.600, -1.242, 1.094, 
         0.001, 0.548, -0.229, -0.797, 0.711, -0.425, 0.010]

u = np.array(list1)
v = np.array(list2)

#Subtract each item in v from each item in u; square results
diff = u - v
sq = diff**2

#sum of the result of the squared differences
x = 0
for val in sq:
    x += val

# finally take square root; result == Eucladian Distance!
rt = math.sqrt(x)
print("Eucladian Distance:", rt)