import sys
from collections import deque


def bfs(tomato):
    queue = deque()
    queue.extend(tomato)
    level = deque()
    cnt = 0
    while queue:
        size = len(queue)
        for _ in range(size):
            cur = queue.popleft()
            for i, j in zip(dx,dy):
                x = i + cur[0]
                y = j + cur[1]
                if 0 <= x < m and 0 <= y < n:
                    if graph[y][x] is 0:
                        queue.append((x,y))
                        graph[y][x] = 1
        cnt += 1
    return cnt - 1


m, n = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for i in range(n)]
visit = [[0 for j in range(m)] for i in range(n)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
tomato = deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] is 1:
            tomato.append((j,i))

res = bfs(tomato)

for i in graph:
    if 0 in i:
        print(-1)
        exit()

print(res)