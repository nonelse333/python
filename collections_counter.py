#https://www.hackerrank.com/challenges/collections-counter

from collections import Counter
n = int(input())
stock = Counter(map(int, input().split()))
sn = int(input())

income = 0
for i in range (sn):
    size, price = map(int, input().split())
    if stock[size]:
        income += price 
        stock[size] -= 1
print(income)

