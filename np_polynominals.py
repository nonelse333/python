#https://www.hackerrank.com/challenges/np-polynomials

import numpy
a = list(map(float, input().split()))
n = int(input())
print(numpy.polyval(a, n))
