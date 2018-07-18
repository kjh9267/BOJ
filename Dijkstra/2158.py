import sys
from queue import PriorityQueue

v, r, c = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
inf = float('inf')
pq = PriorityQueue()
pq.put((0,0,0,v))
res = [[inf for __ in range(c)] for _ in range(r)]
res[0][0] = 0

while pq.qsize():
    dist, x, y, vel = pq.get()
    if dist > res[y][x]:
        continue
    for i, j in zip(dx,dy):
        xx = x + i
        yy = y + j
        if 0 <= xx < c and 0 <= yy < r:
            diff = graph[y][x] - graph[yy][xx]
            time = 1/vel
            if res[yy][xx] > dist + time:
                res[yy][xx] = dist + time
                pq.put((res[yy][xx], xx, yy,  vel*(2**diff)))

print("{:.2f}".format(res[r-1][c-1]))