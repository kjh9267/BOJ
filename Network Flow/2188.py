from sys import stdin
from collections import deque


def match(start,end):
    graph[start].append(end)
    capacity[start].append(1)
    flow[start].append(0)
    graph[end].append(start)
    capacity[end].append(0)
    flow[end].append(0)


def bfs():
    queue = deque()
    queue.append(0)
    way = [-1 for _ in range(sink+1)]
    while queue:
        x = queue.popleft()
        for i, j in enumerate(graph[x]):
            if capacity[x][i] - flow[x][i] > 0 and way[j] is -1:
                queue.append(j)
                way[j] = x
                if j is sink:
                    return way
    return way


n, m = map(int, stdin.readline().split())
sink = n + m + 1
graph = [[] for _ in range(sink + 1)]
capacity = [[] for _ in range(sink + 1)]
flow = [[] for _ in range(sink + 1)]
total = 0

for i in range(1,n+1):
    match(0,i)

for i in range(n+1,sink):
    match(i,sink)

for i in range(1,n+1):
    a = list(map(int, stdin.readline().split()))[1:]
    for j in a:
        match(i,n+j)

while True:
    res = bfs()
    if res[sink] is -1:
        break
    f = float('inf')
    node = sink
    while node is not 0:
        y = graph[res[node]].index(node)
        if f > capacity[res[node]][y] - flow[res[node]][y]:
            f = capacity[res[node]][y] - flow[res[node]][y]
        node = res[node]
    node = sink
    while node is not 0:
        y = graph[res[node]].index(node)
        z = graph[node].index(res[node])
        flow[res[node]][y] += f
        flow[node][z] -= f
        node = res[node]
    total += f
print(total)