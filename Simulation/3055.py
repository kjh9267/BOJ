import sys
from collections import deque


def water():
    for ii in range(r):
        for jj in range(c):
            if graph[ii][jj] is '*':
                for i, j in zip(dx,dy):
                    xx = jj + i
                    yy = ii + j
                    if 0 <= yy < r and 0 <= xx < c:
                        if graph[yy][xx] == 'S' or graph[yy][xx] == '.':
                            graph[yy][xx] = '**'
    for i in range(r):
        for j in range(c):
            if graph[i][j] == '**':
                graph[i][j] = '*'


def bfs(y, x):
    queue = deque()
    queue.append((x,y))
    level = deque()
    water()
    while queue:
        a = queue.popleft()
        for i, j in zip(dx,dy):
            xx = a[0] + i
            yy = a[1] + j
            if 0 <= yy < r and 0 <= xx < c and way[yy][xx] is -1:
                if graph[yy][xx] == '.' or graph[yy][xx] == 'D':
                    level.append((xx,yy))
                    way[yy][xx] = a
                    if graph[yy][xx] == 'D':
                        return way
        if not queue:
            water()
            while level:
                queue.append(level.popleft())


r, c = map(int,sys.stdin.readline().split())
graph = []
way = [[-1 for j in range(c)] for i in range(r)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
cnt = 0

for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            way = bfs(i,j)
        if graph[i][j] == 'D':
            node = (j,i)

if way is None:
    print('KAKTUS')
else:
    while way[node[1]][node[0]] is not -1:
        cnt += 1
        node = way[node[1]][node[0]]
    print(cnt)