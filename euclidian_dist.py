# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import math as math
# Eucladian Distance
print("Eucladian Distance (Step-by-Step): ")
print("")

list1 = [0.819, -0.329, 0.248, -0.677, 0.643, 0.825, 
         0.896, -0.595, 0.619, 0.135, 0.497, 0.744, 1.117]
list2 = [0.164, 0.869, 0.186, 0.523, -0.075, 0.977, 
         -1.212, 0.724, -0.778, 0.939, -1.162, -1.289, -0.406]
list3 = [-0.937, -0.368, -0.393, 0.249, -0.573, -0.034,
         0.083, 0.009, 0.010, -0.881, 0.437, 0.295, -0.776]

list4 = [-1.023, -0.480, 0.049, 0.600, -1.242, 1.094, 
         0.001, 0.548, -0.229, -0.797, 0.711, -0.425, 0.010]

u = np.array(list1)
v = np.array(list4)

print("[Step 1]: Initial Arrays Given: \n")
print("Array u = ", u)
print("Array v = ", v)
print('\n')

#Subtract each item in v from each item in u; square results
diff = u - v
print("[Step 2] Subtraction Phase: \n", diff)
print('\n')

sq = diff**2
print("[Step 3] Squares Phase: \n", sq)
print('\n')

#sum of the result of the squared differences
x = 0
for val in sq:
    x += val
print("[Step 4] Sum of Squares Phase: \n", x)
print('\n')

# finally take square root; result == Eucladian Distance!
rt = math.sqrt(x)
print("[Step 5] Outer Sqrt, Final Result: \n",rt)