#https://www.hackerrank.com/challenges/np-min-and-max/problem

import numpy
N, M = map(int, input().split())
l = []
for i in range(N):
    a = list(map(int, input().split()))
    l.append(a)
my_array = numpy.array(l)
result = numpy.min(my_array, axis = 1)
print(max(result))


