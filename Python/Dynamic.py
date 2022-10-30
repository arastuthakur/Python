"""
Assume the Data set of 20x20. [Generate data set using random number
generator]. An application is to be created to generate a sub matrix of size
[nxn], [n is input]
For example, if n=5 then matrix selected will be [5x5] from 20x20 available
matrix.
The application generate a path to travel between “SOURCE AND SOURCE”.
"""

import random
#For Random Number Generation
import numpy as np 
#To use array using numpy module
from python_tsp.exact import solve_tsp_dynamic_programming
#For Travelling Salesman Dynamic Approach
import timeit 
#To Calculate Time Consumed
start = timeit.default_timer()
#Start of the Timer
array = np.random.randint(20, size=(20, 20))
#Creation of An Array of Random Integers
print("The Main Array",array)
#Display Main Array
size_of_matrix = (random.randint(1,20))
#Defining Sub Matrix Size.
print("The size of Sub matrix is  ",size_of_matrix,"X",size_of_matrix )
#Display Size of New Matrix to be extracted
val = (array[0:size_of_matrix,0:size_of_matrix])
#Defining a new variable val to store a matrix of specified size 
print("The extracted sub array",val)
#Displaying The Sub Array
distance_matrix = np.array(val)
#Storing Sub Array in Variable Distance Matrix
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
#Inbuilt Library of Python to Solve TSP using Dynamic Programming
print(f"The vertex columns are as follows {permutation}")
#Displaying the permutation columns
print(f"The total cost from source to source vertex is: {distance}")
#Displaying the cost to reach source to source
stop = timeit.default_timer()
#Stopping the execution timer
print('Time: ', stop - start)
#Displaying The Execution Timer