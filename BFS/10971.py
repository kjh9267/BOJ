import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append([0,0,[0]])
    while queue:
        cur, cost, visited = queue.popleft()
        for i in range(n):
            if graph[cur][i] > 0 and i not in visited:
                queue.append([i,cost + graph[cur][i], visited + [i]])
            elif graph[cur][i] > 0 and len(visited) == n and i is 0:
                res.append(cost + graph[cur][0])


n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
res = []

bfs()
print(min(res))