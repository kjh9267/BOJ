import sys
from queue import PriorityQueue
import copy

def bfs():
    pq = PriorityQueue()
    temp = [False for _ in range(n)]
    temp[k] = True
    tmp = [[False for _ in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                tmp[i][j] = True
    dist = [float('inf') for _ in range(n)]
    dist[k] = 0
    pq.put((graph[k][1],[k, dist[:],temp[:], copy.deepcopy(tmp)]))
    # check = [[False for _ in range(n)] for i in range(n)]
    while not pq.empty():
        a, b = pq.get()
        cur, dist, visited, check = b
        print(cur, dist, visited)

        for nxt in range(n):
            if graph[cur][nxt][0] > 0 and dist[nxt] > dist[cur] + graph[cur][nxt][0]:
                tmp2 = [[False for _ in range(n)] for i in range(n)]
                for i in range(n):
                    for j in range(n):
                        tmp2[i][j] = check[i][j]
                tmp2[cur][nxt] = True
                temp2 = copy.deepcopy(visited)
                for idx, boolean in enumerate(path[cur][nxt]):
                    if boolean:
                        temp2[idx] = True
                tmp3 = dist[:]
                tmp3[nxt] = tmp3[cur] + graph[cur][nxt][0]
                pq.put((tmp3[nxt],[nxt,tmp3, temp2, tmp2]))
                if False not in temp2:
                    print(tmp3)
                    res.append(tmp3[nxt])
                    continue


n, k = map(int,input().split())
graph = [[[] for __ in range(n)] for _ in range(n)]
for i in range(n):
    line = list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        graph[i][j] = [line[j],j]

res = []
path = [[[False for _ in range(n)] for col in range(n)] for row in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j][0] > graph[i][k][0] + graph[k][j][0]:
                graph[i][j][0] = graph[i][k][0] + graph[k][j][0]
                path[i][j][i] = True
                path[i][j][k] = True
                path[i][j][j] = True
            else:
                path[i][j][i] = True
                path[i][j][j] = True
for i in graph:
    print(i)
for i, j in enumerate(graph):
    graph[i] = sorted(j)
for i in graph:
    print(i)
for i in path:
    print(i)
bfs()
print(res)