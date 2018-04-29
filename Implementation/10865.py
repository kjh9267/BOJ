import sys

n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

for i in range(n):
    print(len(graph[i]))