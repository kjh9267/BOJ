import sys

n, m = map(int,sys.stdin.readline().split())
graph = [[]for _ in range(n)]
inf = float('inf')
res = [inf for _ in range(n)]
res[0] = 0

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1].append((b-1, c))

for i in range(n):
    for j in range(n):
        for node, dist in graph[j]:
            if res[j] != inf and res[node] > res[j] + dist:
                res[node] = res[j] + dist
                if i == n - 1:
                    print(-1)
                    exit()

for i in range(1,n):
    if res[i] == 0 or res[i] == inf:
        print(-1)
    else:
        print(res[i])