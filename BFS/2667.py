def bfs(graph,visit,start):
    queue = [start]
    home = 0
    while len(queue) is not 0:
        x = queue.pop(0)
        if visit[x[0]][x[1]] == 0:
            visit[x[0]][x[1]] = 1
            home += 1
            if x[0] - 1 >= 0:
                if graph[x[0]-1][x[1]] == 1 and [x[0]-1,x[1]] not in queue and visit[x[0]-1][x[1]] == 0:
                    queue.append([x[0]-1,x[1]])
            if x[1] - 1 >= 0:
                if graph[x[0]][x[1]-1] == 1 and [x[0],x[1]-1] not in queue and visit[x[0]][x[1]-1] == 0:
                    queue.append([x[0],x[1]-1])
            if x[0] + 1 < n:
                if graph[x[0]+1][x[1]] == 1 and [x[0]+1,x[1]] not in queue and visit[x[0]+1][x[1]] == 0:
                    queue.append([x[0]+1,x[1]])
            if x[1] + 1 < n:
                if graph[x[0]][x[1]+1] == 1 and [x[0],x[1]+1] not in queue and visit[x[0]][x[1]+1] == 0:
                    queue.append([x[0],x[1]+1])
    return home
n = input()
graph = [map(int,list(raw_input())) for i in range(n)]
visit = [[0 for j in range(n)] for i in range(n)]
cnt = 0
res = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visit[i][j] == 0:
            res.append(bfs(graph,visit,[i,j]))
            cnt += 1
res = sorted(res)
print cnt
for i in range(cnt):
    print res[i]