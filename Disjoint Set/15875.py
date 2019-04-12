# https://www.acmicpc.net/problem/15875


import sys
sys.setrecursionlimit(99000000)


class FlatElement:
    def __init__(self, height, x, y):
        self.height = height
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.height < other.height


def init():
    for row in range(1, H + 1):
        for col in range(1, W + 1):
            flat.append(FlatElement(graph[row][col], col, row))
    flat.sort()

    visited[0][0] = True
    parent[0] = inf
    dfs(0, 0)
    # for i in visited:
    #     print(i)


def dfs(x, y):
    for xx, yy in zip(dx, dy):
        next_x = x + xx
        next_y = y + yy
        if next_y < 0 or next_y >= H + 2 or next_x < 0 or next_x >= W + 2:
            continue
        if graph[y][x] > graph[next_y][next_x]:
            continue
        if not visited[next_y][next_x]:
            visited[next_y][next_x] = True
            # print(next_x, next_y, next_y * W + next_x)
            parent[next_y * (W + 2) + next_x] = inf
            dfs(next_x, next_y)


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif parent[x] < parent[y]:
        parent[x] += parent[y]
        parent[y] = x
    else:
        parent[y] += parent[x]
        parent[x] = y


def farming():
    for ele in flat:
        idx = ele.y * (W + 2) + ele.x
        if visited[ele.y][ele.x]:
            continue
        for x, y in zip(dx, dy):
            next_x = ele.x + x
            next_y = ele.y + y
            next_idx = next_y * (W + 2) + next_x
            if visited[next_y][next_x]:
                continue
            # if parent[next_idx] == -1:
            merge(idx, next_idx)
        # print(parent, idx)


if __name__ == '__main__':
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    inf = float('inf')
    input = __import__('sys').stdin.readline
    H, W = map(int,input().split())
    size = (H + 2) * (W + 2)
    graph = [[0 for row in range(W + 2)] for col in range(H + 2)]
    for row in range(1, H + 1):
        graph[row][1:-1] = list(map(int,input().split()))
    visited = [[False for col in range(W + 2)] for row in range(H + 2)]
    parent = [-1 for _ in range(size)]
    flat = list()
    init()
    # for i in flat:
    #     print(i.height)
    farming()
    # print(parent)
    # print(list(range(H*W)))
    # for i in visited:
    #     print(i)
    res = -min(parent)
    print(0 if res == -inf else res)