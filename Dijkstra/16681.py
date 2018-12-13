import sys
from queue import PriorityQueue


def dijkstra(start):
    pq = PriorityQueue()
    res = [inf for _ in range(N)]
    pq.put((0,start))
    res[start] = 0
    while not pq.empty():
        dist, node = pq.get()
        if dist > res[node]:
            continue
        for nxt, cst in zip(graph[node],cost[node]):
            if height[node] >= height[nxt]:
                continue
            if res[nxt] > dist + cst:
                res[nxt] = dist + cst
                pq.put((res[nxt],nxt))
    return res


N, M, D, E = map(int,sys.stdin.readline().split())
height = list(map(int,sys.stdin.readline().split()))
graph = [[] for _ in range(N)]
cost = [[] for _ in range(N)]
inf = float('inf')

for _ in range(M):
    a, b, n = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)
    cost[a-1].append(n)
    cost[b-1].append(n)

visited = [[False,False] for _ in range(N)]
up = dijkstra(0)
down = dijkstra(N-1)
result = -9223372036854775808

for i in range(N):
    if up[i] == inf or down[i] == inf:
        continue
    result = max(result, height[i] * E - (up[i] + down[i]) * D)


if result != -9223372036854775808:
    print(result)
else:
    print("Impossible")