import sys
from collections import deque


def bfs():
    queue = deque()
    visit = [0 for _ in range(n)]
    for u in range(n):
        if visit[u] is 0:
            queue.append(u)
            team = [u]
            while queue:
                x = queue.popleft()
                for i, j in enumerate(graph[x]):
                    if i is u:
                        continue
                    if j is 1 and visit[i] is 0:
                        queue.append(i)
                        visit[i] = 1
                        team.append(i)
            teams.append(team)


n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = float('inf')
graph = [[inf for __ in range(n)] for _ in range(n)]
teams = []

for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1
    graph[b-1][a-1] = 1

bfs()

for v in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            if graph[i][j] > graph[i][v] + graph[v][j]:
                graph[i][j] = graph[i][v] + graph[v][j]

for i in range(n):
    for j in range(n):
        if graph[i][j] == inf:
            graph[i][j] = 0

res = [[max(graph[j]) for j in i if graph[j]] for i in teams]
output = []

print(len(teams))

for i in range(len(teams)):
    x = min(res[i])
    output.append(teams[i][res[i].index(x)] + 1)

for i in sorted(output):
    print(i)