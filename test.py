MIS = lambda: map(int,input().split())

import heapq
def dijkstra(adj, source):
    n = len(adj)-1; dist = [float('inf')]*(n+1)
    dist[source] = 0; PQ = [(0, source)]
    while PQ:
        d, u = heapq.heappop(PQ)
        if dist[u] != d: continue
        for v, c in adj[u]:
            if dist[v] > d+c: dist[v] = d+c; heapq.heappush(PQ, (d+c, v))
    return dist

n, m = MIS()
adj = [[] for i in range(n+1)]
for i in range(m):
    a, b, dfl, add, t = MIS()
    if t <= 10: cost = dfl
    else: cost = dfl + add*(t-10)
    cost = 1000000000*cost + 1
    adj[a].append((b,cost))
d = dijkstra(adj, 1)[n]
if d == float('inf'): print("It is not a great way.")
else: print(d//1000000000, d%1000000000+1)