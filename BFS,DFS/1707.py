import sys
from collections import deque

k = int(sys.stdin.readline())

for _ in range(k):
    v, e = map(int,sys.stdin.readline().split())
    graph = [[] for _ in range(v)]
    visit = [0 for _ in range(v)]

    for __ in range(e):
        a, b = map(int,sys.stdin.readline().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    key = False
    for j in range(v):
        if visit[j] is 0:
            queue = deque()
            queue.append(j)
            visit[j] = 1
            while queue:
                cur = queue.popleft()
                for i in graph[cur]:
                    if visit[i] is 0:
                        visit[i] = -visit[cur]
                        queue.append(i)
                    elif visit[i] is visit[cur]:
                        key = True
                        break

    if key:
        print('NO')
    else:
        print('YES')