import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(start)
    level = deque()
    visit[start[0]][start[1]] = [1,1,1]
    cnt = 0
    while queue:
        y, x, d, z = queue.popleft()
        for i, j in enumerate(zip(dx,dy)):
            print(list(enumerate(zip(dx,dy))))
            for u in range(3):
                xx = x + j[0][u]
                yy = y + j[1][u]
                if 0 <= xx < n and 0 <= yy < m:
                    if graph[yy][xx] == '1':
                        break
                    if visit[yy][xx][u] is 0 and graph[yy][xx] == '0':
                        visit[yy][xx][u] = 1
                        level.append((yy,xx,i,z + move(d,i)))
                        if xx == end[1] and y == end[0]:
                            print(cnt)
                            print(z)
                            print(move(d,end[2]))
                            return cnt + z + move(d, end[2])
        if not queue:
            queue.extend(level)
            level.clear()
            cnt += 1
        print(queue)


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
visit = [[[0,0,0] for j in range(n)] for i in range(m)]

for i in range(4):
    start[i] -= 1

for i in range(3):
    end[i] -= 1
print(start, end)
print(bfs())