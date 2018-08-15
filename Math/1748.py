import sys

N = int(sys.stdin.readline())
res = 0
cur = 1

while cur <= N:
    res += N - cur + 1
    cur *= 10

print(res)