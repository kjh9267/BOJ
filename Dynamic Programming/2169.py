# https://www.acmicpc.net/problem/2169
import sys
sys.setrecursionlimit(999999999)


def dfs(x, y, go):
    if y == N - 1 and x == M - 1:
        return grid[y][x]
    if dp[y][x][go] != -inf:
        return dp[y][x][go]
    value = -inf
    for idx, diff in enumerate(zip(dx, dy)):
        diff_x, diff_y = diff
        next_x = x + diff_x
        next_y = y + diff_y
        if not (0 <= next_y < N and 0 <= next_x < M):
            continue
        if visited[next_y][next_x]:
            continue
        visited[next_y][next_x] = True
        value = max(value, dfs(next_x, next_y, idx))
        visited[next_y][next_x] = False
    dp[y][x][go] = max(dp[y][x][go], value + grid[y][x])
    return dp[y][x][go]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (-1, 0, 1)
    dy = (0, 1, 0)
    inf = float('inf')
    N, M = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    dp = [[[-inf for _ in range(3)] for _ in range(M)] for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    visited[0][0] = True
    print(dfs(0, 0, 0))
