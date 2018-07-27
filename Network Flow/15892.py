import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(0)
    level[0] = 0
    while queue:
        cur = queue.popleft()
        for index, nxt in enumerate(graph[cur]):
            if level[nxt] is -1 and capacity[cur][index] > flow[cur][index]:
                level[nxt] = level[cur] + 1
                queue.append(nxt)
    return level[n-1] != -1


def dfs(cur,f):
    if cur == n-1:
        return f
    temp = work[cur]
    for i in range(temp,len(graph[cur])):
        work[cur] = i
        nxt = graph[cur][i]
        if capacity[cur][i] > flow[cur][i] and level[nxt] == level[cur] + 1:
            df = dfs(nxt,min(f, capacity[cur][i] - flow[cur][i]))
            if df > 0:
                flow[cur][i] += df
                flow[nxt][graph[nxt].index(cur)] -= df
                return df
    return 0


n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]
capacity = [[] for _ in range(n)]
flow = [[] for _ in range(n)]
inf = float('inf')
total = 0

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    capacity[a-1].append(c)
    capacity[b-1].append(c)
    flow[a-1].append(0)
    flow[b-1].append(0)

while True:
    level = [-1 for _ in range(n)]
    if not bfs():
        break
    work = [0 for _ in range(n)]
    while True:
        f = dfs(0,inf)
        if not f:
            break
        total += f

print(total)