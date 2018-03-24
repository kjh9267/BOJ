import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(start)
    level = deque()
    cnt = 0
    res = []
    while queue:
        y, x, d, z = queue.popleft()
        visit[y][x] = 1
        for i, j in enumerate(zip(dx,dy)):
            for u in range(3):
                xx = x + j[0][u]
                yy = y + j[1][u]
                if 0 <= xx < n and 0 <= yy < m:
                    if graph[yy][xx] == '1':
                        break
                    if visit[yy][xx] is 0 and graph[yy][xx] == '0' and (yy,xx,i,z+move(d,i)) not in level:
                        level.append((yy,xx,i,z + move(d,i)))
                        if xx == end[1] and yy == end[0]:
                            res.append(cnt + z + move(d,i) + move(i,end[2]) + 1)
        if not queue:
            queue.extend(level)
            level.clear()
            cnt += 1
    return res


def move(s,e):
    if s is 0:
        if e is 0:
            return 0
        if e is 2 or e is 3:
            return 1
        if e is 1:
            return 2
    if s is 1:
        if e is 1:
            return 0
        if e is 2 or e is 3:
            return 1
        if e is 0:
            return 2
    if s is 2:
        if e is 2:
            return 0
        if e is 0 or e is 1:
            return 1
        if e is 3:
            return 2
    if s is 3:
        if e is 3:
            return 0
        if e is 0 or e is 1:
            return 1
        if e is 2:
            return 2


m, n = map(int,sys.stdin.readline().split())
graph = [sys.stdin.readline().split() for _ in range(m)]
start = list(map(int,sys.stdin.readline().split()))
start.append(1)
end = list(map(int,sys.stdin.readline().split()))
dx = ((1,2,3),(-1,-2,-3),(0,0,0),(0,0,0))
dy = ((0,0,0),(0,0,0),(1,2,3),(-1,-2,-3))
visit = [[0 for j in range(n)] for i in range(m)]

for i in range(4):
    start[i] -= 1

for i in range(3):
    end[i] -= 1

if start[0] == end[0] and start[1] == end[1]:
    print(move(start[2],end[2]))
else:
    print(min(bfs()))