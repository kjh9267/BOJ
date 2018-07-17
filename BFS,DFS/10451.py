import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    graph = list(map(int,sys.stdin.readline().split()))
    visit = [0 for _ in range(n)]
    cnt = 0
    for i in graph:
        if visit[i-1] is 0:
            queue = deque()
            queue.append(i-1)
            visit[i-1] = 1
            while queue:
                cur = queue.popleft()
                if visit[graph[cur]-1] is 0:
                    queue.append(graph[cur]-1)
                    visit[graph[cur]-1] = 1
            cnt += 1
    print(cnt)