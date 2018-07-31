import sys
from collections import deque


def match(u,v,c):
    graph[u].append(v)
    cost[u][v] = c
    capacity[u][v] = 1
    cost[v][u] = -c
    graph[v].append(u)


n, m = map(int,sys.stdin.readline().split())
inf = float('inf')
end = n + m + 2
graph = [[] for _ in range(end)]
capacity = [[0 for __ in range(end)] for _ in range(end)]
flow = [[0 for __ in range(end)] for _ in range(end)]
cost = [[0 for __ in range(end)] for _ in range(end)]
total = 0
res = 0

for i in range(1,n+1):
    x = list(map(int,sys.stdin.readline().split()))

    for j in range(1,x[0]*2+1,2):
        match(i,x[j]+n,x[j+1])

for i in range(1,n+1):
    match(0,i,0)

for i in range(n+1,end-1):
    match(i,end-1,0)

while True:
    queue = deque()
    queue.append(0)
    way = [-1 for _ in range(end)]
    dist = [inf for _ in range(end)]
    inQ = [False for _ in range(end)]
    inQ[0] = True
    dist[0] = 0
    while queue:
        cur = queue.popleft()
        inQ[cur] = False
        for nxt in graph[cur]:
            if capacity[cur][nxt] - flow[cur][nxt] > 0 and dist[nxt] > dist[cur] + cost[cur][nxt]:
                dist[nxt] = dist[cur] + cost[cur][nxt]
                way[nxt] = cur
                if not inQ[nxt]:
                    queue.append(nxt)
                    inQ[nxt] = True

    if way[end-1] is -1:
        break

    node = end-1
    while node is not 0:
        total += cost[way[node]][node]
        flow[way[node]][node] += 1
        flow[node][way[node]] -= 1
        node = way[node]

    res += 1

print(res)
print(total)