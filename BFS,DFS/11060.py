import sys
from collections import deque

n = int(sys.stdin.readline())
graph = list(map(int,sys.stdin.readline().split()))
queue = deque()
queue.append(0)
visit = [-1 for _ in range(n)]
visit[0] = 0

while queue:
    cur = queue.popleft()
    for i in range(1,graph[cur] + 1):
        if cur + i < n and visit[cur + i] is -1:
            visit[cur + i] = visit[cur] + 1
            queue.append(cur + i)
            if cur + i == n - 1:
                break

print(visit[-1])