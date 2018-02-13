import sys
from collections import deque


def danger():
    for i, j in fire:
        for x, y in zip(dx,dy):
            xx = i + x
            yy = j + y
            if graph[yy][xx] == '.' or graph[yy][xx] == '@':
                graph[yy][xx] = '*'
                temp.append((xx,yy))
    fire.clear()
    for i in temp:
        fire.append(i)
    temp.clear()


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    level = deque()
    way = [[-1 for j in range(w+2)] for i in range(h+2)]
    danger()
    while queue:
        b = queue.popleft()
        for i, j in zip(dx,dy):
            xx = b[0] + i
            yy = b[1] + j
            if graph[yy][xx] == '.' or graph[yy][xx] == '$':
                if way[yy][xx] is -1:
                    level.append((xx,yy))
                    way[yy][xx] = (b[0],b[1])
                    if graph[yy][xx] == '$':
                        node.append((xx,yy))
                        return way
        if not queue:
            danger()
            for i in level:
                queue.append(i)
            level.clear()


t = int(sys.stdin.readline())
dx = (1,0,-1,0)
dy = (0,1,0,-1)
temp = deque()

for _ in range(t):
    w, h = map(int,sys.stdin.readline().split())
    graph = [['$' for _ in range(w+2)]]
    node = []
    cnt = 0

    for __ in range(h):
        a = list('$' + sys.stdin.readline().rstrip() + '$')
        graph.append(a)

    graph.append(['$' for _ in range(w+2)])
    fire = deque()

    for i in range(1,h+1):
        for j in range(1,w+1):
            if graph[i][j] == '*':
                fire.append((j,i))
            elif graph[i][j] == '@':
                start = (j,i)

    way = bfs(start[0], start[1])

    if way is None:
        print('IMPOSSIBLE')
    else:
        node = node[0]
        while way[node[1]][node[0]] is not -1:
            cnt += 1
            node = way[node[1]][node[0]]
        print(cnt)