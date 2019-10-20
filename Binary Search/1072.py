# https://www.acmicpc.net/problem/1072


def bs(Z):
    lo = -1
    hi = inf
    while lo + 1 < hi:
        mid = (lo + hi) >> 1
        if int((Y + mid) / (X + mid) * 100) > Z:
            hi = mid
        else:
            lo = mid
    return -1 if hi == inf else hi


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = 2_000_000_001
    X, Y = map(int,input().split())
    Z = int(Y / X * 100 + 0.00000001)
    print(bs(Z))
