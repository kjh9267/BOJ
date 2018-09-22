import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append((0,0,0))
    level = deque()
    visit[0][0] = [1 for _ in range(k+1)]
    cnt = 0
    while queue:
        a = queue.popleft()
        for i, j in zip(dx,dy):
            x = i + a[0]
            y = j + a[1]
            if 0 <= x < c and 0 <= y < r:
                if visit[y][x][a[2]] is 0 and graph[y][x] is 0:
                    level.append((x,y,a[2]))
                    visit[y][x][a[2]] = 1
                    if x == c-1 and y == r-1:
                        return cnt + 1
        if a[2] < k:
            for i, j in zip(dx2,dy2):
                x = i + a[0]
                y = j + a[1]
                if 0 <= x < c and 0 <= y < r:
                    if visit[y][x][a[2]+1] is 0 and graph[y][x] is 0:
                        level.append((x,y,a[2]+1))
                        visit[y][x][a[2]+1] = 1
                        if x == c-1 and y == r-1:
                            return cnt + 1
        if not queue:
            queue.extend(level)
            level.clear()
            cnt += 1


k = int(sys.stdin.readline())
c, r = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]
visit = [[[0 for u in range(k+1)] for j in range(c)] for i in range(r)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
dx2 = (1,-1,2,-2,2,-2,1,-1)
dy2 = (2,2,1,1,-1,-1,-2,-2)

if r is 1 and c is 1:
    print(0)
    exit()

res = bfs()

if res is None:
    print(-1)
else:
    print(res)