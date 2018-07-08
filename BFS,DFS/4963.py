import sys
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[y][x] = True
    while queue:
        a = queue.popleft()
        for i, j in zip(dx,dy):
            xx = i + a[0]
            yy = j + a[1]
            if 0 <= xx < w and 0 <= yy < h and graph[yy][xx] is 1 and visit[yy][xx] is False:
                queue.append((xx,yy))
                visit[yy][xx] = True


dx = (1,0,-1,0,1,1,-1,-1)
dy = (0,1,0,-1,1,-1,1,-1)

while True:
    w, h = map(int,sys.stdin.readline().split())

    if w is 0 and h is 0:
        break

    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]
    visit = [[False for __ in range(w)] for _ in range(h)]
    result = 0

    for i in range(h):
        for j in range(w):
            if graph[i][j] is 1 and visit[i][j] is False:
                bfs(j,i)
                result += 1

    print(result)