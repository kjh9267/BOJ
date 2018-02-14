import sys
from collections import deque


def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    while queue:
        z = queue.popleft()
        visit[z[1]][z[0]] = 1
        for i, j in zip(dx,dy):
            y = z[1] + j
            x = z[0] + i
            if graph[y][x] > 0 and visit[y][x] is 0:
                queue.append((x,y))


n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
land = deque()
temp = deque()
dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)
time = 0

for i in range(1, n - 1):
    for j in range(1, m - 1):
        if graph[i][j] > 0:
            land.append([j, i, graph[i][j], 0])

while True:
    visit = [[0 for j in range(m)]for i in range(n)]
    cnt = 0

    for i in land:
        if visit[i[1]][i[0]] is 0:
            cnt += 1
            if cnt > 1:
                print(time)
                exit()
            bfs(i[0],i[1])
        for a, b in zip(dx,dy):
            x = a + i[0]
            y = b + i[1]
            if graph[y][x] <= 0:
                i[3] += 1

    time += 1

    if not land:
        print(0)
        break

    for i in land:
        i[2] -= i[3]
        graph[i[1]][i[0]] -= i[3]
        i[3] = 0

    for i in land:
        if i[2] > 0:
            temp.append(i)

    land.clear()

    for i in temp:
        land.append(i)

    temp.clear()