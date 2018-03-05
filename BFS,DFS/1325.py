import sys
from collections import deque


def bfs(num):
    queue = deque()
    queue.append(num)
    visit = [0 for _ in range(n)]
    visit[num] = 1
    while queue:
        x = queue.popleft()
        for i in graph[x]:
            if visit[i] == 0:
                queue.append(i)
                visit[i] = 1
    return sum(visit)


n, m = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]
res = [0 for _ in range(n)]

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[b-1].append(a-1)

for i in range(n):
    res[i] = bfs(i)

y = max(res)
result = []

for i, j in enumerate(res):
    if j == y:
        result.append('{}'.format(i+1))

print(" ".join(result))