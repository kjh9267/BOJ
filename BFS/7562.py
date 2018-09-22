import sys
from collections import deque


def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    while queue:
        c = queue.popleft()
        for i, j in zip(dx,dy):
            x = c[0] + i
            y = c[1] + j
            if 0 <= x < n and 0 <= y < n and way[y][x] is -1 and graph[y][x] != 's':
                queue.append((x,y))
                way[y][x] = (c[0],c[1])
                if graph[y][x] == 'e':
                    return


t = int(sys.stdin.readline())
dx = (2,1,2,1,-1,-2,-2,-1)
dy = (1,2,-1,-2,-2,-1,1,2)

for _ in range(t):
    n = int(sys.stdin.readline())
    graph = [['x' for j in range(n)] for i in range(n)]
    way = [[-1 for j in range(n)] for i in range(n)]
    a, b = map(int,sys.stdin.readline().split())
    graph[b][a] = 's'
    e, r = map(int,sys.stdin.readline().split())
    graph[r][e] = 'e'
    cnt = 0

    if a is e and b is r:
        print(0)
        continue

    bfs(a,b)

    while way[r][e] != -1:
        cnt += 1
        r,e = way[r][e][1], way[r][e][0]

    print(cnt)