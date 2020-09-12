#https://www.hackerrank.com/challenges/exceptions

n = int(input())
for i in range(n):
    try:
        a, b = map(int, input().split())
        print(a // b)
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)

