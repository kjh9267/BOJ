# https://www.acmicpc.net/problem/17130
import sys
sys.setrecursionlimit(999999999)


def dfs(x, y):
    value = grid[y][x]
    if dp[y][x] != -inf:
        return dp[y][x]
    dp[y][x] = 0 if value == 'O' else -inf + 1
    plus = 1 if value == 'C' else 0

    for diff_x, diff_y in zip(dx, dy):
        next_x = x + diff_x
        next_y = y + diff_y
        if not can_go(next_x, next_y):
            continue
        dp[y][x] = max(dp[y][x], dfs(next_x, next_y) + plus)

    return dp[y][x]


def can_go(x, y):
    return 0 <= x < M and 0 <= y < N and grid[y][x] != '#'


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = 100_000_000
    dx = (1, 1, 1)
    dy = (-1, 0, 1)
    N, M = map(int, input().split())
    grid = [input().rstrip() for _ in range(N)]
    dp = [[-inf for _ in range(M)] for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if grid[row][col] == 'R':
                res = dfs(col, row)
                print(-1 if res < 0 else res)