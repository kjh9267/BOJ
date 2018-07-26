import sys


def dfs(node):
    if visit[graph[node]] is 0:
        visit[graph[node]] = 1
        dfs(graph[node])
    if visit[graph[node]] is 1:
        visit[graph[node]] = 2
        dfs(graph[node])
    if visit[node] is 1:
        visit[node] = 0
    return visit[node]


n = int(sys.stdin.readline())
graph = [int(sys.stdin.readline()) - 1 for _ in range(n)]
visit = [0 for _ in range(n)]

for i in range(n):
    if visit[i] is 0:
        visit[i] = 1
        dfs(i)

print(visit.count(2))
for i,j in enumerate(visit):
    if j is 2:
        print(i+1)
