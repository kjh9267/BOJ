import sys

t = int(sys.stdin.readline())

for _ in range(t):
    sx, sy, ex, ey = map(int,sys.stdin.readline().split())
    n = int(sys.stdin.readline())
    res = 0

    for __ in range(n):
        x, y, r = map(int,sys.stdin.readline().split())

        if (sx - x)**2 + (sy - y)**2 < r**2:
            if (ex - x)**2 + (ey - y)**2 > r**2:
                res += 1
        else:
            if (ex - x)**2 + (ey - y)**2 < r**2:
                res += 1

    print(res)