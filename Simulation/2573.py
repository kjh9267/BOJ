import sys
from collections import deque


def bfs(a,b):
    queue = deque()
    queue.append([a,b])
    while queue:
        z = queue.popleft()
        visit[z[0]][z[1]] = 1
        for i in range(4):
            y = z[0] + dy[i]
            x = z[1] + dx[i]
            if 0 <= y < n and 0 <= x < m:
                if graph[y][x] > 0 and visit[y][x] is 0 and [y,x] not in queue:
                    queue.append([y,x])


def melt(a,b):
    for i in range(4):
        y = a + dy[i]
        x = b + dx[i]
        if 0 <= y < n and 0 <= x < m :
            if graph[y][x] <= 0:
                melvisit[a][b] += 1


n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
cnt = 0
land = 0

while True:
    melvisit = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0:
                melt(i,j)

    for i in range(n):
        for j in range(m):
            graph[i][j] -= melvisit[i][j]

    visit = [[0 for j in range(m)]for i in range(n)]
    land = 0

    for i in range(n):
        for j in range(m):
            if graph[i][j] > 0 and visit[i][j] is 0:
                bfs(i,j)
                land += 1

    cnt += 1
    if land > 1:
        print(cnt)
        break

    for i in range(n):
        for j in range(m):
            if graph[i][j] < 0:
                graph[i][j] = 0

    if sum([sum(graph[i]) for i in range(n)]) is 0:
        print(0)
        break