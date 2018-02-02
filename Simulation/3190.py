from sys import stdin
from collections import deque


def move(direction):
    if b is 'D':
        if direction is 3:
            direction -= 3
        else:
            direction += 1
    elif b is 'L':
        if direction is 0:
            direction += 3
        else:
            direction -= 1
    return direction

n = int(stdin.readline())
k = int(stdin.readline())
graph = [['x' for j in range(n)] for i in range(n)]
graph[0][0] = 's'
snake = deque()
snake.append([0,0])
dx = [1,0,-1,0]
dy = [0,1,0,-1]
direction = 0
cnt = 0
prev = 0

for _ in range(k):
    r, c = map(int,stdin.readline().split())
    graph[r-1][c-1] = 'o'

l = int(stdin.readline())
for _ in range(l):
    a, b = stdin.readline().split()
    a = int(a) - cnt
    for i in range(a):
        cnt += 1
        head = snake[-1]
        tail = snake[0]
        y = head[0] + dy[direction]
        x = head[1] + dx[direction]
        if 0 <= y < n and 0 <= x < n and graph[y][x] is not 's':
            if graph[y][x] is 'x':
                graph[tail[0]][tail[1]] = 'x'
                snake.popleft()
            snake.append([y,x])
            graph[y][x] = 's'
        else:
            print(cnt)
            exit()
    direction = move(direction)
print(cnt+1)