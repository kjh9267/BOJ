# https://www.acmicpc.net/problem/17090


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return False
    if parent[x] > parent[y]:
        parent[y] += parent[x]
        parent[x] = y
        if out[x]:
            out[x] = False
            out[y] = True
        return True
    else:
        if out[y]:
            out[y] = False
            out[x] = True
        parent[x] += parent[y]
        parent[y] = x
        return True


def convert(char):
    if char == 'U':
        return 0
    elif char == 'R':
        return 1
    elif char == 'D':
        return 2
    else:
        return 3


def flat(x, y):
    return y * M + x


def dfs(x, y):
    stack = list()
    stack.append((x,y))
    while stack:
        x, y = stack.pop()
        cur = flat(x, y)
        direction = convert(graph[y][x])
        next_x = x + dx[direction]
        next_y = y + dy[direction]
        if next_x < 0 or next_x >= M or next_y < 0 or next_y >= N:
            out[find(cur)] = True
            return
        nxt = flat(next_x, next_y)
        if not merge(cur, nxt):
            return
        if visited[next_y][next_x]:
            return
        visited[next_y][next_x] = True
        stack.append((next_x, next_y))


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (0,1,0,-1)
    dy = (-1,0,1,0)
    N, M = map(int,input().split())
    graph = [list(input().rstrip()) for _ in range(N)]
    visited = [[False for col in range(M)] for row in range(N)]
    parent = [-1 for _ in range(N * M)]
    out = [False for _ in range(N * M)]
    res = 0

    for row in range(N):
        for col in range(M):
            if visited[row][col]:
                continue
            visited[row][col] = True
            dfs(col, row)

    for idx, check in enumerate(out):
        if check:
            res -= parent[idx]

    print(res)