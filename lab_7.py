#Exercise 1
# Import the math package
import math
# Import radians function of math package
from math import radians

# Definition of radius
r = 0.43


# Calculate C
C = 2 * math.pi * r

# Calculate A
A = math.pi * r ** 2

# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))

#Exercise 2
# Definition of radius
r = 192500

# Travel distance of Moon if 12 degrees. Store in dist.
dist = radians(12)

# Print out dist
print(dist)


#Exercise 3
import scipy
from scipy.linalg import inv as my_inv

list = my_inv([[1,2], [3,4]])
print(list)