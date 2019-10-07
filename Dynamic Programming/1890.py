# https://www.acmicpc.net/problem/1890

import sys
sys.setrecursionlimit(999999999)


def dfs(x, y):
    if x >= N or y >= N:
        return 0
    if x == N - 1 and y == N - 1:
        return 1
    if dp[y][x] != -1:
        return dp[y][x]
    dp[y][x] = 0
    dp[y][x] += dfs(x + grid[y][x], y)
    dp[y][x] += dfs(x, y + grid[y][x])
    return dp[y][x]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    dp = [[-1 for _ in range(N)] for _ in range(N)]
    print(dfs(0, 0))