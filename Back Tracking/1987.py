import sys


def dfs(x,y,a):
    global cnt
    if cnt < a:
        cnt = a
    for i,j in zip(dx,dy):
        xx = x + i
        yy = y + j
        if xx < 0 or xx >= c or yy < 0 or yy >= r:
            continue
        if visit[graph[yy][xx]]:
            continue
        visit[graph[yy][xx]] = 1
        dfs(xx,yy,a+1)
        visit[graph[yy][xx]] = 0


r, c = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for i in range(r)]

for i in range(r):
    graph[i] = list(map(lambda x: ord(x) - 65,graph[i]))

visit = [0 for _ in range(26)]
visit[graph[0][0]] = 1
dx = (1,0,-1,0)
dy = (0,1,0,-1)
cnt = 0

dfs(0,0,1)

print(cnt)