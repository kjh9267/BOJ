import sys

t = int(sys.stdin.readline())
inf = float('inf')

for _ in range(t):
    n, m, w = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(n)]
    res = [inf for _ in range(n)]
    res[0] = 0
    key = False

    for __ in range(m):
        a, b, c = map(int,sys.stdin.readline().split())
        graph[a - 1].append([b - 1, c])
        graph[b - 1].append([a - 1, c])

    for __ in range(w):
        a, b, c = map(int,sys.stdin.readline().split())
        graph[a - 1].append([b - 1, -c])

    for i in range(n):
        for j in range(n):
            for node, dist in graph[j]:
                if res[j] != 'inf' and res[node] > res[j] + dist:
                    res[node] = res[j] + dist
                    if i == n-1:
                        key = True

    if key is True:
        print('YES')
    else:
        print('NO')