# https://www.acmicpc.net/problem/2146

import sys
sys.setrecursionlimit(999999999)


def dfs(x, y, cnt):
    if visited[y][x]:
        return
    visited[y][x] = True
    candi[cnt].append((x, y))
    new_grid[y][x] = cnt
    for i, j in zip(dx, dy):
        xx = i + x
        yy = j + y
        if not (0 <= xx < N and 0 <= yy < N):
            continue
        if grid[yy][xx] == '0':
            continue
        dfs(xx,yy,cnt)


def bfs(cnt):
    queue = __import__('collections').deque()
    visited = [[False for _ in range(N)] for __ in range(N)]
    for i in candi[cnt]:
        queue.append(i)
        visited[i[1]][i[0]] = True
    res = 0
    while queue:
        size = len(queue)
        res += 1
        for _ in range(size):
            cur = queue.popleft()
            for i, j in zip(dx, dy):
                x = cur[0] + i
                y = cur[1] + j
                if not (0 <= x < N and 0 <= y < N):
                    continue
                if visited[y][x]:
                    continue
                if new_grid[y][x] != cnt and new_grid[y][x] != 0:
                    return res - 1
                queue.append((x, y))
                visited[y][x] = True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    grid = [list(input().split()) for _ in range(N)]
    new_grid = [[0 for _ in range(N)] for __ in range(N)]
    candi = dict()
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    res = float('inf')
    visited = [[False for _ in range(N)] for __ in range(N)]
    cnt = 0

    for row in range(N):
        for col in range(N):
            if visited[row][col] or grid[row][col] == '0':
                continue
            cnt += 1
            candi[cnt] = list()
            dfs(col, row, cnt)

    for i in candi.keys():
        res = min(res, bfs(i))

    print(res)