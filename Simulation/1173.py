import sys

N, m, M, T, R = map(int,sys.stdin.readline().split())
time = 0
cur = m
n = 0

if m + T > M:
    print(-1)
    exit()

while True:
    if cur + T <= M:
        cur += T
        time += 1
        n += 1
    else:
        cur -= R
        time += 1
        if cur < m:
            cur = m
    if n == N:
        print(time)
        break