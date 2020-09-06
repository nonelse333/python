#https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
word, num = input().split()
per = list(permutations(sorted(word), int(num)))
for i in per:
    print("".join(i))

