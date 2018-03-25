import sys
from queue import PriorityQueue


inf = float('inf')
dx = (1,0,-1,0)
dy = (0,1,0,-1)
cnt = 1
while True:
    n = int(sys.stdin.readline())

    if n is 0:
        break

    graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
    pq = PriorityQueue()
    pq.put((graph[0][0],(0,0)))
    res = [[inf for __ in range(n)] for _ in range(n)]
    res[0][0] = graph[0][0]

    while pq.qsize():
        dist, node = pq.get()
        if dist > res[node[1]][node[0]]:
            continue
        for i, j in zip(dx,dy):
            x = i + node[0]
            y = j + node[1]
            if 0 <= x < n and 0 <= y < n:
                if res[y][x] > dist + graph[y][x]:
                    res[y][x] = dist + graph[y][x]
                    pq.put((res[y][x],(x,y)))

    print('Problem {}: {}'.format(cnt,res[n-1][n-1]))
    cnt += 1