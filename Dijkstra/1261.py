import sys
from queue import PriorityQueue

m, n = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
pq = PriorityQueue()
pq.put((0,(0,0)))
inf = float('inf')
res = [[inf for _ in range(m)] for __ in range(n)]
res[0][0] = 0
dx = (1,0,-1,0)
dy = (0,1,0,-1)

while pq.qsize():
    dist, node = pq.get()
    if res[node[1]][node[0]] < dist:
        continue
    for i, j in zip(dx,dy):
        x = i + node[0]
        y = j + node[1]
        if 0 <= x < m and 0 <= y < n:
            if res[y][x] > dist + graph[y][x]:
                res[y][x] = dist + graph[y][x]
                pq.put((res[y][x],(x,y)))

print(res[n-1][m-1])