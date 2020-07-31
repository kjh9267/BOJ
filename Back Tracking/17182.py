# https://www.acmicpc.net/problem/17182
import sys
sys.setrecursionlimit(999999999)


def floyd():
    for mid in range(N):
        for start in range(N):
            for end in range(N):
                grid[start][end] = min(grid[start][end], grid[start][mid] + grid[mid][end])


def dfs(cur, dist, visited):
    if dist > res[0]:
        return
    if visited == 2 ** N - 1:
        res[0] = min(res[0], dist)
        return
    for nxt in range(N):
        if visited & (1 << nxt) != 0:
            continue
        dfs(nxt, dist + grid[cur][nxt], visited | (1 << nxt))


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, K = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = 0
    res = [float('inf')]
    floyd()
    dfs(K, 0, 1 << K)

    print(res[0])