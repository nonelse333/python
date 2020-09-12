#https://www.hackerrank.com/challenges/py-collections-namedtuple/

from collections import namedtuple

n = int(input())
index = input().split()
index_a = " ".join(index)

total = 0
for i in range(n):
    list = namedtuple("list",index_a)
    i1, i2, i3, i4 = input().split()
    s = list(i1,i2,i3,i4)
    total += int(s.MARKS)
print(total / n)

