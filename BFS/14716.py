import sys


def bfs(start):
    queue = [start]
    while len(queue) is not 0:
        x = queue.pop(0)
        visit[x[0]][x[1]] = 1
        for i in range(-1,2):
            for j in range(-1,2):
                if i != 0 or j != 0:
                    if 0 <= x[0]+i < m and 0 <= x[1]+j < n:
                        if graph[x[0]+i][x[1]+j] == 1:
                            if visit[x[0]+i][x[1]+j] == 0:
                                if [x[0]+i,x[1]+j] not in queue:
                                    queue.append([x[0]+i,x[1]+j])

m, n = map(int,sys.stdin.readline().split())
graph = [map(int,sys.stdin.readline().split()) for i in range(m)]
visit = [[0 for i in range(n)] for j in range(m)]
cnt = 0

for a in range(m):
    for b in range(n):
        if graph[a][b] == 1 and visit[a][b] == 0:
            bfs([a,b])
            cnt += 1
print cnt