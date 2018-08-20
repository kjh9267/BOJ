import sys
from collections import deque

n, l = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n)]
line = [list(map(int,sys.stdin.readline().split()))[:-1] for _ in range(l)]

for i in range(l):
    for j in range(len(line[i])):
        line[i][j] -= 1

for i, j in enumerate(line):
    for u in j:
        graph[u].append(i)

s, e = map(int,sys.stdin.readline().split())
s -= 1
e -= 1

if set(graph[s]).intersection(graph[e]):
    print(0)
    exit()

queue = deque()
queue.append(s)
level = deque()
visit = [0 for _ in range(l)]
cnt = 0

for i in graph[s]:
    visit[i] = 1

while queue:
    x = queue.popleft()
    for i in graph[x]:
        for j in line[i]:
            for u in graph[j]:
                if visit[u] is 0:
                    visit[u] = 1
                    level.append(j)
                    if e in line[u]:
                        print(cnt + 1)
                        exit()
    if not queue:
        queue.extend(level)
        level.clear()
        cnt += 1

print(-1)