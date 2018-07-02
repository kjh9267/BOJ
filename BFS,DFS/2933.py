from collections import deque
import sys


def bfs(x,y):
    key = True
    queue = deque()
    queue.append((x,y))
    visit[y][x] = cluster
    while queue:
        a = queue.popleft()
        for i, j in zip(dx,dy):
            xx = a[0] + i
            yy = a[1] + j
            if 0 <= xx < c and 0 <= yy < r and visit[yy][xx] is 0 and graph[yy][xx] == 'x':
                visit[yy][xx] = cluster
                queue.append((xx,yy))
                if yy == r - 1:
                    key = False
    return key


def throw(direction):
    if direction is 1:
        for i in range(c):
            if graph[r-height][i] == 'x':
                graph[r-height][i] = '.'
                return
    else:
        for i in range(c-1,-1,-1):
            if graph[r-height][i] == 'x':
                graph[r-height][i] = '.'
                return


def is_bottom(x,y):
    for i in range(y+1,r):
        if visit[i][x] == cluster:
            return False
    return True


def down(cluster):
    cnt = float('inf')
    for i in range(r-2,-1,-1):
        for j in range(c):
            if graph[i][j] == 'x' and visit[i][j] == cluster and is_bottom(j,i):
                temp = 1
                for u in range(i+1,r):
                    if u+1 < r and graph[u+1][j] == 'x':
                        cnt = min(temp,cnt)
                        break
                    elif u == r-1:
                        cnt = min(temp,cnt)
                        break
                    temp += 1

    for i in range(r-2,-1,-1):
        for j in range(c):
            if visit[i][j] == cluster:
                graph[i+cnt][j] = 'x'
                graph[i][j] = '.'
    #print(cnt, cluster)


r, c = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for _ in range(r)]
n = int(sys.stdin.readline())
arrow = deque(map(int,sys.stdin.readline().split()))
dx = (1,0,-1,0)
dy = (0,1,0,-1)
direction = 1

while arrow:
    height = arrow.popleft()
    cluster = 0
    temp = 0
    visit = [[0 for j in range(c)] for i in range(r)]
    throw(direction)
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 'x' and visit[i][j] is 0:
                cluster += 1
                if bfs(j,i):
                    temp = cluster
    cluster = temp
    if cluster is not 0:
        down(cluster)
    direction *= -1
'''
    for i,j in zip(graph,visit):
        print(''.join(i), j)
    print()
'''
for i in graph:
    print(''.join(i))