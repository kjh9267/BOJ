from collections import deque
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = float('inf')
graph = [[inf for __ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    if graph[a-1][b-1] > c:
        graph[a-1][b-1] = c

for v in range(n):
    for s in range(n):
        for e in range(n):
            if s == e:
                continue
            if graph[s][e] > graph[s][v] + graph[v][e]:
                graph[s][e] = graph[s][v] + graph[v][e]

for i in range(n):
    for j in range(n):
        if graph[i][j] == inf:
            graph[i][j] = 0

for i in graph:
    print(" ".join(map(str,i)))