import sys
from queue import PriorityQueue


def dijkstra(start):
    pq = PriorityQueue()
    pq.put((0,start))
    res = [inf for _ in range(n)]
    res[start] = 0
    while pq.qsize():
        dist, node = pq.get()
        if res[node] < dist:
            continue
        for i, j in graph[node]:
            if res[i] > j + dist:
                res[i] = j + dist
                pq.put((res[i],i))
    return res


n, e = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n)]

for _ in range(e):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1].append((b-1,c))
    graph[b-1].append((a-1,c))

g, h = map(int,sys.stdin.readline().split())
g -= 1
h -= 1
inf = float('inf')
res1 = dijkstra(0)
res2 = dijkstra(g)
res3 = dijkstra(h)
result = min(res1[g] + res2[h] + res3[n-1], res1[h] + res3[g] + res2[n-1])

if result == inf:
    print(-1)
else:
    print(result)