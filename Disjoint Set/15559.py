# https://www.acmicpc.net/problem/15559
import sys
sys.setrecursionlimit(999999999)


def dfs(x, y):
    cur = y * M + x
    if grid[y][x] == 'N':
        idx = 0
    elif grid[y][x] == 'E':
        idx = 1
    elif grid[y][x] == 'S':
        idx = 2
    else:
        idx = 3
    xx = x + dx[idx]
    yy = y + dy[idx]
    if not (0 <= xx < M and 0 <= yy < N):
        return
    nxt = yy * M + xx
    if merge(cur, nxt):
        return
    dfs(xx, yy)


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return True
    if parent[x] > parent[y]:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x
    return False


if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    N, M = map(int,input().split())
    grid = [list(input().rstrip()) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    parent = [-1 for _ in range(N * M)]
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    cnt = 0

    for row in range(N):
        for col in range(M):
            dfs(col, row)

    for idx in parent:
        if idx < 0:
            cnt += 1

    print(cnt)