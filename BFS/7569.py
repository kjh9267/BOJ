import sys
from collections import deque

m, n, h = map(int,sys.stdin.readline().split())
graph = [[list(map(int,sys.stdin.readline().split())) for _ in range(n)] for __ in range(h)]
dx = (1,0,-1,0,0,0)
dy = (0,1,0,-1,0,0)
dz = (0,0,0,0,1,-1)
queue = deque()
cnt = -1

for i in range(h):
    for j in range(n):
        for u in range(m):
            if graph[i][j][u] is 1:
                queue.append((u,j,i))

while queue:
    size = len(queue)
    for _ in range(size):
        cur = queue.popleft()
        for i, j, u in zip(dx,dy,dz):
            x = cur[0] + i
            y = cur[1] + j
            z = cur[2] + u
            if 0 <= x < m and 0 <= y < n and 0 <= z < h and graph[z][y][x] is 0:
                graph[z][y][x] = 1
                queue.append((x,y,z))
    cnt += 1

if 0 in [u for i in graph for j in i for u in j]:
    print(-1)
else:
    print(cnt)