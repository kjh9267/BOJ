import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(start)
    level = deque()
    visit[start[0]][start[1]] = 1
    while queue:
        x, y, d = queue.popleft()
        for i, j in enumerate(zip(dx,dy)):
            xx = x + j[0]
            yy = y + j[1]
            if 0 <= xx < m and 0 <= yy < n:
                if visit[yy][xx] is 0 and graph[yy][xx] == '0':



n, m = map(int,sys.stdin.readline().split())
graph = [sys.stdin.readline().split() for _ in range(n)]
start = tuple(map(int,sys.stdin.readline().split()))
end = tuple(map(int,sys.stdin.readline().split()))
dx = (1,-1,0,0)
dy = (0,0,1,-1)
visit = [[0 for j in range(m)] for i in range(n)]