#Program Name: population-dispersion.py
#Assignment Module 3
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210523

#Importing Statistics Module
import statistics
import math

answer1 = statistics.pvariance([1,3,4,2,6,5,3,4,5,2])
print(f'Pvarience is: {answer1:0.2f}')

answer2 = statistics.pstdev([1,3,4,2,6,5,3,4,5,2])
print(f'Pstandard deviation is: {answer2:0.2f}')

answer3 = math.sqrt(statistics.pvariance([1,3,4,2,6,5,3,4,5,2]))

print(f'Square root of the pvariance is: {answer3:0.2f}')




