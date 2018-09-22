def bfs(graph,start,visit,end):
    queue = [start]
    level = []
    cnt = 0
    k = 0
    while len(queue) != 0:
        if end in queue:
            k = 1
            break
        x = queue.pop(0)
        visit.append(x)
        for i in range(len(graph)):
            if graph[x-1][i] == 1 and i+1 not in visit and i+1 not in level:
                level.append(i+1)
        if len(queue) == 0:
            for i in range(len(level)):
                queue.append(level[i])
            level = []
            cnt += 1
    return cnt, k
n = input()
start, end = map(int,raw_input().split())
graph = [[0 for j in range(n)] for i in range(n)]
visit = []
m = input()
for i in range(m):
    a, b = map(int,raw_input().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1
res = bfs(graph,start,visit,end)
if res[1] == 0:
    print -1
else:
    print res[0]