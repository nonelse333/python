#https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(input())
m = list(map(int,input().split()))
mset = set(m)
N = int(input())
n = list(map(int,input().split()))
nset = set(n)

A = mset.union(nset) - mset.intersection(nset)
for i in sorted(A):
    print(i)

