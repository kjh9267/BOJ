import sys
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[y][x] = 1
    while queue:
        a = queue.popleft()
        for i, j in zip(dx,dy):
            xx = i + a[0]
            yy = j + a[1]
            if 0 <= xx < n and 0 <= yy < n:
                if graph[yy][xx] > h and visit[yy][xx] is 0:
                    queue.append((xx,yy))
                    visit[yy][xx] = 1


n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
res = []

for i in range(101):
    visit = [[0 for __ in range(n)] for _ in range(n)]
    h = i
    cnt = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] > h and visit[i][j] is 0:
                bfs(j,i)
                cnt += 1
    res.append(cnt)

print(max(res))