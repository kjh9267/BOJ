import sys
from collections import deque

n = int(sys.stdin.readline())
graph = list(map(int,sys.stdin.readline().split()))
start = int(sys.stdin.readline())
visit = [0 for _ in range(n)]
queue = deque()
queue.append(start-1)
visit[start-1] = 1

while queue:
    current = queue.popleft()
    back = current - graph[current]
    front = current + graph[current]
    if 0 <= back and visit[back] is 0:
        visit[back] = 1
        queue.append(back)
    if front < n and visit[front] is 0:
        visit[front] = 1
        queue.append(front)

print(sum(visit))