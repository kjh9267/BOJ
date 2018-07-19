import sys

S = sys.stdin.readline().rstrip()

a = S.count('pi') * 2
b = S.count('ka') * 2
c = S.count('chu') * 3

if a + b + c == len(S):
    print("YES")
else:
    print("NO")