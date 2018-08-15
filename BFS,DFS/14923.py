import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())
Hy, Hx = map(lambda x: int(x) - 1,sys.stdin.readline().split())
Ey, Ex = map(lambda x: int(x) - 1,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[[-1,-1] for _ in range(M)] for __ in range(N)]
dx = (0, 1, 0, -1)
dy = (-1, 0, 1, 0)

queue = deque()
queue.append((Hx,Hy,0))
visited[Hy][Hx] = [0,0]

while queue:
    x, y, z = queue.popleft()

    for i, j in zip(dx,dy):
        xx = x + i
        yy = y + j
        if 0 <= xx < M and 0 <= yy < N:
            if graph[yy][xx] is 0 and visited[yy][xx][z] is -1:
                visited[yy][xx][z] = visited[y][x][z] + 1
                queue.append((xx,yy,z))
            elif z is 0 and graph[yy][xx] is 1 and visited[yy][xx][z] is -1:
                visited[yy][xx][1] = visited[y][x][z] + 1
                queue.append((xx,yy,1))
            if xx == Ex and yy == Ey:
                print(max(visited[y][x]) + 1)
                exit()

print(-1)