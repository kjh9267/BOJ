def dfs(graph, visit, start):
    stack = [start]
    color = graph[start[0]][start[1]]
    while len(stack) != 0:
        x = stack.pop(-1)
        if visit[x[0]][x[1]] == 0:
            visit[x[0]][x[1]] = 1
            if x[1]+1 < len(graph):
                if graph[x[0]][x[1]+1] == color and visit[x[0]][x[1]+1] != 1:
                    stack.append([x[0],x[1]+1])
            if x[0]+1 < len(graph):
                if graph[x[0]+1][x[1]] == color and visit[x[0]+1][x[1]] != 1:
                    stack.append([x[0]+1,x[1]])
            if x[0]-1 >= 0:
                if graph[x[0]-1][x[1]] == color and visit[x[0]-1][x[1]] != 1:
                    stack.append([x[0]-1,x[1]])
            if x[1] - 1 >= 0:
                if graph[x[0]][x[1]-1] == color and visit[x[0]][x[1]-1] != 1:
                    stack.append([x[0],x[1]-1])
    return visit
n = input()
graph = [raw_input()for i in range(n)]
graph2 = [[0for i in range(n)]for j in range(n)]
visit = [[0 for j in range(n)] for i in range(n)]
cnt = 0
cnt2 = 0
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            dfs(graph,visit,[i,j])
            cnt += 1
for i in range(n):
    graph2[i] = graph[i].replace('R','G')
visit = [[0 for j in range(n)] for i in range(n)]
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            dfs(graph2,visit,[i,j])
            cnt2 += 1
print cnt, cnt2