#https://www.hackerrank.com/challenges/py-collections-deque/

from collections import deque
d = deque()
n = int(input())
for _ in range(n):
    op = list(input().split())
    if op[0] == "append":
        d.append(int(op[1]))
    elif op[0] == "appendleft":
        d.appendleft(int(op[1]))
    elif op[0] == "pop":
        d.pop()
    elif op[0] == "popleft":
        d.popleft()
print(*d)

