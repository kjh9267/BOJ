import sys
from collections import deque


def bfs():
    visit = [[False for __ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if graph[y][x] is 2 and visit[y][x] is False:
                queue = deque()
                queue.append((x,y))
                visit[y][x] = True
                while queue:
                    a = queue.popleft()
                    for i, j in zip(dx,dy):
                        xx = a[0] + i
                        yy = a[1] + j
                        if 0 <= xx < m and 0 <= yy < n:
                            if graph[yy][xx] == 0 and visit[yy][xx] is False:
                                visit[yy][xx] = True
                                graph[yy][xx] = 2
                                queue.append((xx,yy))


def check():
    cnt = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] is 0:
                cnt += 1
    return cnt


n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
temp_graph = [[0 for _ in range(m)] for __ in range(n)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
res = 0

for i in range(n):
    for j in range(m):
        temp_graph[i][j] = graph[i][j]

for ay in range(n):
    for ax in range(m):
        for by in range(n):
            for bx in range(m):
                for cy in range(n):
                    for cx in range(m):
                        if graph[ay][ax] == 0 and graph[by][bx] == 0 and graph[cy][cx] == 0:
                            if [ay,ax] != [by,bx] and [ay,ax] != [cy,cx] and [by,bx] != [cy,cx]:
                                graph[ay][ax] = 1
                                graph[by][bx] = 1
                                graph[cy][cx] = 1
                                bfs()
                                res = max(res,check())
                                for i in range(n):
                                    for j in range(m):
                                        graph[i][j] = temp_graph[i][j]

print(res)