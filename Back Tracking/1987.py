import sys


def asc(graph,x,y):
        return ord(graph[y][x]) - 65


def dfs(x,y,a):
    global cnt
    if cnt < a:
        cnt = a
    if a == max:
        return
    for i,j in zip(dx,dy):
        xx = x + i
        yy = y + j
        if 0 <= xx < c and 0 <= yy < r:
            z = asc(graph, xx, yy)
            if visit[z]:
                continue
            visit[z] = 1
            dfs(xx,yy,a+1)
            visit[z] = 0


r, c = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for i in range(r)]
max = len(set([i for row in graph for i in row]))
visit = [0 for _ in range(26)]
visit[asc(graph,0,0)] = 1
dx = (1,0,-1,0)
dy = (0,1,0,-1)
cnt = 0

dfs(0,0,1)

print(cnt)