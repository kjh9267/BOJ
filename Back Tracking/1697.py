import sys
from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        for i in graph[a]:
            if way[i] == -1:
                queue.append(i)
                way[i] = a
                if i == k:
                    return


n, k = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(100001)]
way = [-1 for _ in range(100001)]
cnt = 0

for i in range(1,100001):
    graph[i].append(i-1)

for i in range(100000):
    graph[i].append(i+1)

for i in range(100001):
    if i*2 < 100001:
        graph[i].append(i*2)

bfs(n)

while k != n:
    cnt += 1
    k = way[k]

print(cnt)