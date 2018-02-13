import sys
from collections import deque


def danger():
    for j, i in water:
        for x, y in zip(dx,dy):
            xx = x + j
            yy = y + i
            if 0 <= yy < r and 0 <= xx < c:
                if graph[yy][xx] == 'S' or graph[yy][xx] == '.':
                    graph[yy][xx] = '*'
                    temp.append((xx,yy))
    water.clear()
    for i in temp:
        water.append(i)
    temp.clear()


def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    level = deque()
    danger()
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
            danger()
            while level:
                queue.append(level.popleft())


r, c = map(int,sys.stdin.readline().split())
graph = []
way = [[-1 for j in range(c)] for i in range(r)]
water = deque()
temp = deque()
dx = (1,0,-1,0)
dy = (0,1,0,-1)
cnt = 0

for _ in range(r):
    graph.append(list(sys.stdin.readline().rstrip()))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            start = (j,i)
        elif graph[i][j] == 'D':
            node = (j,i)
        elif graph[i][j] == '*':
            water.append((j,i))

way = bfs(start[0], start[1])

if way is None:
    print('KAKTUS')
else:
    while way[node[1]][node[0]] is not -1:
        cnt += 1
        node = way[node[1]][node[0]]
    print(cnt)