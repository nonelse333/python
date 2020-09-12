#https://www.hackerrank.com/challenges/validating-the-phone-number

n = int(input())
for _ in range(n):
    a = input()
    if len(a) == 10 and (a.startswith("7") or a.startswith("8") or a.startswith("9")) and a.isdigit():
        print("YES")
    else:
        print("NO")

