#  https://www.acmicpc.net/problem/3482

import sys
from collections import deque


def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[y][x] = 0
    while queue:
        x, y = queue.popleft()
        for c, r in zip(dx, dy):
            next_x = x + c
            next_y = y + r
            if graph[next_y][next_x] == '.' and visit[next_y][next_x] is -1:
                visit[next_y][next_x] = visit[y][x] + 1
                queue.append((next_x, next_y))


def long():
    temp, x, y = 0, 0, 0
    for i in range(R):
        for j in range(C):
            if temp < visit[i][j]:
                temp = visit[i][j]
                x, y = j, i
    return temp, x, y


if __name__ == '__main__':
    T = int(sys.stdin.readline())
    dx = (1,0,-1,0)
    dy = (0,1,0,-1)

    for _ in range(T):
        C, R = map(int, sys.stdin.readline().split())
        graph = [list(sys.stdin.readline().rstrip()) for _ in range(R)]
        visit = [[-1 for col in range(C)] for row in range(R)]
        key = False
        x, y = 0, 0

        for row in range(1,R-1):
            for col in range(1,C-1):
                cnt = 0
                for x, y in zip(dx,dy):
                    next_x = col + x
                    next_y = row + y
                    if graph[next_y][next_x] == '#':
                        cnt += 1
                if cnt is 3:
                    x, y = col, row
                    key = True
                    break
            if key:
                break

        bfs(x, y)
        temp, x, y = long()
        visit = [[-1 for col in range(C)] for row in range(R)]
        bfs(x, y)
        res, x, y = long()

        print("Maximum rope length is {}.".format(res))