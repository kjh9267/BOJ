import sys
from collections import deque


def bfs(z,y,x):
    queue = deque()
    queue.append((x,y,z))
    level = deque()
    visit[z][y][x] = 1
    cnt = 0
    while queue:
        a = queue.popleft()
        for i, j, u in zip(dx,dy,dz):
            xx = a[0] + i
            yy = a[1] + j
            zz = a[2] + u
            if 0 <= xx < c and 0 <= yy < r and 0 <= zz < l:
                if graph[zz][yy][xx] != '#' and visit[zz][yy][xx] is 0:
                    level.append((xx,yy,zz))
                    visit[zz][yy][xx] = 1
                    if graph[zz][yy][xx] == 'E':
                        return cnt + 1
        if not queue:
            queue.extend(level)
            level.clear()
            cnt += 1


while True:
    l, r, c = map(int, sys.stdin.readline().split())

    if l is 0 and r is 0 and c is 0:
        break

    graph = [[] for _ in range(l)]
    visit = [[[0 for ___ in range(c)] for __ in range(r)] for _ in range(l)]
    dx = (0,0,0,0,1,-1)
    dy = (0,0,1,-1,0,0)
    dz = (1,-1,0,0,0,0)

    for i in range(l):
        for _ in range(r):
            graph[i].append(list(sys.stdin.readline().rstrip()))
        sys.stdin.readline()

    for i in range(l):
        for j in range(r):
            for u in range(c):
                if graph[i][j][u] == 'S':
                    res = bfs(i,j,u)

    if res is None:
        print('Trapped!')
    else:
        print('Escaped in {} minute(s).'.format(res))