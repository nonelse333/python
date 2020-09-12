#https://www.hackerrank.com/challenges/np-sum-and-prod

import numpy
N, M = map(int, input().split())

my_array = numpy.array([input().split() for i in range(N)], int)
print(numpy.prod((numpy.sum(my_array,axis=0))))
