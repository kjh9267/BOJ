# https://www.acmicpc.net/problem/1074
import sys
sys.setrecursionlimit(999999999)


def solve(x, y, size):

    if x == C and y == R:
        print(cnt[0])
        return

    size >>= 1

    if x <= C < x + size and y <= R < y + size:
        solve(x, y, size)
    cnt[0] += size * size

    if x + size <= C < x + size * 2 and y <= R < y + size:
        solve(x + size, y, size)
    cnt[0] += size * size

    if x <= C < x + size and y + size <= R < y + size * 2:
        solve(x, y + size, size)
    cnt[0] += size * size

    if x + size <= C < x + size * 2 and y + size <= R < y + size * 2:
        solve(x + size, y + size, size)
    cnt[0] += size * size


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (-1, 0, -1, 0)
    dy = (-1, -1, 0, 0)
    N, R, C = map(int, input().split())
    cnt = [0]
    solve(0, 0, 1 << N)