# https://www.acmicpc.net/problem/1937
import sys
sys.setrecursionlimit(999999999)


def dfs(x, y, depth):
    if dp[y][x] != 0:
        return dp[y][x]
    dp[y][x] = 1
    for i, j in zip(dx, dy):
        xx = x + i
        yy = y + j
        if not (0 <= xx < N and 0 <= yy < N):
            continue
        if grid[yy][xx] <= grid[y][x]:
            continue
        dp[y][x] = max(dp[y][x], dfs(xx, yy, depth + 1) + 1)
    return dp[y][x]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dp = [[0 for _ in range(N)] for _ in range(N)]
    res = 0

    for row in range(N):
        for col in range(N):
            res = max(res, dfs(col, row, 1))

    print(res)

