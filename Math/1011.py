import sys
from math import ceil

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int,sys.stdin.readline().split())
    diff = y - x
    z = diff**0.5
    res = 2 * z - 1

    print(ceil(res))