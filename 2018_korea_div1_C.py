import sys
from queue import PriorityQueue
from collections import deque


def dijkstra(start):
    pq = PriorityQueue()
    res = [inf for _ in range(N)]
    pq.put((0,start))
    res[start] = 0
    while not pq.empty():
        dist, node = pq.get()
        for nxt, cst in zip(graph[node],cost[node]):
            if height[node] >= height[nxt]:
                continue
            if res[nxt] > dist + cst:
                res[nxt] = dist + cst
                pq.put((res[nxt],nxt))
    return res


def bfs(start,flag):
    queue = deque()
    queue.append(start)
    visited[start][flag] = True
    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            if visited[nxt][flag]:
                continue
            if height[cur] < height[nxt]:
                queue.append(nxt)
                visited[nxt][flag] = True
            if visited[nxt] == [True,True]:
                return True
    return False


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
result = [height[i] * E - (up[i] + down[i]) * D for i in range(N)][1:-1]

bfs(0,0)
if bfs(N-1,1):
    print(max(result))
else:
    print("Impossible")