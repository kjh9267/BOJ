import sys
from queue import PriorityQueue

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

inf = float('inf')
pq = PriorityQueue()
pq.put((0,0))
res = [inf for _ in range(n)]
res[0] = 0

while pq.qsize():
    dist, node = pq.get()
    if res[node] < dist:
        continue
    for i in graph[node]:
        if res[i] > dist + 1:
            res[i] = dist + 1
            pq.put((res[i],i))

result = max(res)
print(res.index(result) + 1, result, res.count(result))