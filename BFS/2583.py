def bfs(graph,visit,start):
    queue = [start]
    cnt = 0
    while len(queue) != 0:
        x = queue.pop(0)
        if visit[x[0]][x[1]] == 0:
            visit[x[0]][x[1]] = 1
            cnt += 1
            if x[0]+1 < len(graph) and graph[x[0]+1][x[1]] == 0 and visit[x[0]+1][x[1]] == 0:
                queue.append([x[0]+1,x[1]])
            if x[0]-1 >= 0 and graph[x[0]-1][x[1]] == 0 and visit[x[0]-1][x[1]] == 0:
                queue.append([x[0]-1,x[1]])
            if x[1]+1 < len(graph[0]) and graph[x[0]][x[1]+1] == 0 and visit[x[0]][x[1]+1] == 0:
                queue.append([x[0],x[1]+1])
            if x[1]-1 >= 0 and graph[x[0]][x[1]-1] == 0 and visit[x[0]][x[1]-1] == 0:
                queue.append([x[0],x[1]-1])
    return cnt
m, n, k = map(int,raw_input().split())
graph = [[0 for j in range(n)] for i in range(m)]
for i in range(k):
    a, b, c, d = map(int,raw_input().split())
    for j in range(a,c):
        for v in range(m-d,m-b):
            graph[v][j] = 1
visit = graph
wide = []
for i in range(m):
    for j in range(n):
        if visit[i][j] == 0:
            wide.append(bfs(graph,visit,[i,j]))
print len(wide)
print " ".join(map(str,sorted(wide)))