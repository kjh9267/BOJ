import sys
from collections import deque

T = int(sys.stdin.readline())
inf = float('inf')

for _ in range(T):
    n = int(sys.stdin.readline())
    graph = list(map(lambda x: int(x) - 1,sys.stdin.readline().split()))
    visit = [0 for _ in range(n)]

    for i in range(n):
        if i == graph[i]:
            visit[i] = inf
            continue
        if visit[i] is inf:
            continue
        key = False
        visit[i] = 1
        node = graph[i]
        while True:
            if visit[node] is 0:
                visit[node] = 1
                node = graph[node]
            elif visit[node] is 1 and node != graph[node]:
                key = True
                break
            else:
                break
        if key:
            visit[i] = inf
            node = graph[i]
            while visit[node] is 1:
                visit[node] = inf
                node = graph[node]
            continue
        visit[i] = 0
        node = graph[i]
        while visit[node] is 1:
            visit[node] = 0
            node = graph[node]

    print(visit.count(0))