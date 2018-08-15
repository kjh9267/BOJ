import sys
from collections import deque

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]
cost = [0 for _ in range(n)]
x = list(map(int,sys.stdin.readline().split()))

for i, j in enumerate(x):
    if j is -1:
        continue
    graph[j-1].append(i)

for _ in range(m):
    x, y = map(int,sys.stdin.readline().split())
    cost[x-1] += y

queue = deque()
queue.append(0)
while queue:
    cur = queue.popleft()
    for i in graph[cur]:
        cost[i] += cost[cur]
        if graph[i]:
            queue.append(i)

print(" ".join(map(str,cost)))