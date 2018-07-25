import sys
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for i, j in zip(dx, dy):
            xx = x + i
            yy = y + j
            if graph[yy][xx] == '.' and visit[yy][xx] is -1:
                visit[yy][xx] = visit[y][x] + 1
                queue.append((xx, yy))


def long():
    temp, x, y = 0, 0, 0
    for i in range(R):
        for j in range(C):
            if temp < visit[i][j]:
                temp = visit[i][j]
                x, y = j, i
    return temp, x, y


T = int(sys.stdin.readline())
dx = (1,0,-1,0)
dy = (0,1,0,-1)

for _ in range(T):
    C, R = map(int, sys.stdin.readline().split())
    graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
    visit = [[-1 for __ in range(C)] for _ in range(R)]
    key = False
    x, y = 0, 0

    for i in range(1,R-1):
        for j in range(1,C-1):
            cnt = 0
            for x, y in zip(dx,dy):
                xx = j + x
                yy = i + y
                if graph[yy][xx] == '#':
                    cnt += 1
            if cnt is 3:
                x, y = j, i
                key = True
                break
        if key:
            break

    bfs(x, y)
    temp, x, y = long()
    visit = [[-1 for __ in range(C)] for _ in range(R)]
    bfs(x, y)
    res, x, y = long()

    print("Maximum rope length is {}.".format(res))