import sys
from queue import PriorityQueue

t = int(sys.stdin.readline())
inf = float('inf')

for _ in range(t):
    n, d, c = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    cnt = 0

    for __ in range(d):
        a, b, s = map(int,sys.stdin.readline().split())
        graph[b-1].append((a-1,s))

    res = [inf for _ in range(n)]
    res[c-1] = 0
    pq = PriorityQueue()
    pq.put((0,c-1))

    while pq.qsize():
        dist, node = pq.get()
        for i, j in graph[node]:
            if res[node] < dist:
                continue
            if res[i] > dist + j:
                res[i] = dist + j
                pq.put((res[i],i))

    for i in res:
        if i != inf:
            cnt += 1

    res = set(res)

    if inf in res:
        res.remove(inf)

    print(cnt,max(res))