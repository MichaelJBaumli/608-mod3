#Program Name: bonus.py
#Assignment Module 3
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210523

#Importing Statistics and Math Modules
import statistics
import math
import random

dataset = []



for x in range(1000):
    y = random.randrange(0,1000000)
    dataset.append(y)


answer1 = statistics.pvariance(dataset)

print('The data set is 1000 datapoints generated randrange between 0 and 1,000,000')
print(f'Pvarience is: {answer1:0.2f}')

answer2 = statistics.pstdev(dataset)
print(f'Pstandard deviation is: {answer2:0.2f}')

answer3 = math.sqrt(statistics.pvariance(dataset))

print(f'Square root of the pvariance is: {answer3:0.2f}')