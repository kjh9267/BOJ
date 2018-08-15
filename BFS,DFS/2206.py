import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append((0,0,0))
    level = deque()
    visit[0][0] = [1,1]
    cnt = 1
    while queue:
        a = queue.popleft()
        for i, j in zip(dx,dy):
            x = i + a[0]
            y = j + a[1]
            if 0 <= x < m and 0 <= y < n:
                if x == m-1 and y == n-1:
                    return cnt + 1
                if a[2] is 0 and visit[y][x][0] is 0:
                    if graph[y][x] is 1:
                        level.append((x,y,1))
                        visit[y][x][1] = 1
                    else:
                        level.append((x,y,0))
                        visit[y][x][0] = 1
                elif a[2] is 1 and visit[y][x][1] is 0 and graph[y][x] is 0:
                    level.append((x,y,1))
                    visit[y][x][1] = 1
        if not queue:
            queue.extend(level)
            level.clear()
            cnt += 1


n, m = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().rstrip())) for _ in range(n)]
visit = [[[0,0] for j in range(m)] for i in range(n)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)

if n is 1 and m is 1:
    print(1)
    exit()

res = bfs()

if res is None:
    print(-1)
else:
    print(res)