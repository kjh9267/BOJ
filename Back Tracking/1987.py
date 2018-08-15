import sys


class Res:
    def __init__(self):
        self.res = 1


def dfs(x,y,cnt):
    if res.res < cnt:
        res.res = cnt

    for i, j in zip(dx,dy):
        xx = x + i
        yy = y + j
        if 0 <= xx < c and 0 <= yy < r and not visit[graph[yy][xx]]:
            visit[graph[yy][xx]] = True
            dfs(xx,yy,cnt+1)
            visit[graph[yy][xx]] = False


r, c = map(int,sys.stdin.readline().split())
graph = [list(map(lambda x: ord(x) - 65, sys.stdin.readline().rstrip())) for _ in range(r)]
visit = [False for _ in range(26)]
visit[graph[0][0]] = True
dx = (1,0,-1,0)
dy = (0,1,0,-1)
res = Res()
dfs(0,0,1)
print(res.res)