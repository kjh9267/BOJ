import sys
def bfs(start):
    queue = [start]
    while len(queue) is not 0:
        x = queue.pop(0)
        visit[x[0]][x[1]] = 1
        if 0 <= x[0]-1:
            if graph[x[0]-1][x[1]] > 0:
                if visit[x[0]-1][x[1]] == 0:
                    if [x[0]-1,x[1]] not in queue:
                        queue.append([x[0]-1,x[1]])
        if 0 <= x[1]-1:
            if graph[x[0]][x[1]-1] > 0:
                if visit[x[0]][x[1]-1] == 0:
                    if [x[0],x[1]-1] not in queue:
                        queue.append([x[0],x[1]-1])
        if x[0]+1 < n:
            if graph[x[0]+1][x[1]] > 0:
                if visit[x[0]+1][x[1]] == 0:
                    if [x[0]+1,x[1]] not in queue:
                        queue.append([x[0]+1,x[1]])
        if x[1]+1 < m:
            if graph[x[0]][x[1]+1] > 0:
                if visit[x[0]][x[1]+1] == 0:
                    if [x[0],x[1]+1] not in queue:
                        queue.append([x[0],x[1]+1])
def melt(a,b):
    if 0 <= a - 1:
        if graph[a-1][b] <= 0:
            melvisit[a][b] += 1
    if n > a + 1:
        if graph[a+1][b] <= 0:
            melvisit[a][b] += 1
    if 0 <= b - 1:
        if graph[a][b-1] <= 0:
            melvisit[a][b] += 1
    if m > b + 1:
        if graph[a][b+1] <= 0:
            melvisit[a][b] += 1
n, m = map(int,sys.stdin.readline().split())
graph = [map(int,sys.stdin.readline().split()) for i in range(n)]
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
            if graph[i][j] > 0 and visit[i][j] == 0:
                bfs([i,j])
                land += 1
    cnt += 1
    if land > 1:
        print cnt
        break
    for i in range(n):
        for j in range(m):
            if graph[i][j] < 0:
                graph[i][j] = 0
    if sum([sum(graph[i]) for i in range(n)]) is 0:
        print 0
        break