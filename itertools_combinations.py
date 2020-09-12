#https://www.hackerrank.com/challenges/itertools-combinations/

from itertools import combinations
letter, n = input().split()
N = int(n)+1
for i in range(1, N):
    for j in combinations(sorted(letter),i):
        print ("".join(j))

