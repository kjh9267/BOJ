import sys
from collections import deque

n, p = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n*2 + 1)]
capacity = [[] for _ in range(n*2 + 1)]
flow = [[] for _ in range(n*2 + 1)]
total = 0

for i in range(1,n+1):
    graph[i*2 - 1].append(i*2)
    capacity[i*2 - 1].append(1)
    flow[i*2 - 1].append(0)
    graph[i*2].append(i*2 - 1)
    capacity[i*2].append(0)
    flow[i*2].append(0)

for _ in range(p):
    a, b = map(int, sys.stdin.readline().split())
    graph[a*2].append(b*2 - 1)
    capacity[a*2].append(1)
    flow[a*2].append(0)
    graph[b*2].append(a*2 - 1)
    capacity[b*2].append(1)
    flow[b*2].append(0)
    graph[a*2 - 1].append(b*2)
    capacity[a*2 - 1].append(0)
    flow[a*2 - 1].append(0)
    graph[b*2 - 1].append(a*2)
    capacity[b*2 - 1].append(0)
    flow[b*2 - 1].append(0)

while True:
    queue = deque()
    queue.append(2)
    way = [-1 for _ in range(n*2+1)]
    key = False
    while queue:
        x = queue.popleft()
        for i, j in enumerate(graph[x]):
            if capacity[x][i] - flow[x][i] > 0 and way[j] is -1:
                queue.append(j)
                way[j] = x
                if j is 3:
                    key = True
                    break
        if key is True:
            break
    if way[3] is -1:
        break
    f = float('inf')
    node = 3
    while node is not 2:
        y = graph[way[node]].index(node)
        if f > capacity[way[node]][y] - flow[way[node]][y]:
            f = capacity[way[node]][y] - flow[way[node]][y]
        node = way[node]
    node = 3
    while node is not 2:
        y = graph[way[node]].index(node)
        z = graph[node].index(way[node])
        flow[way[node]][y] += f
        flow[node][z] -= f
        node = way[node]
    total += f
print(total)