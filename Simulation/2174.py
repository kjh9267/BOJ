import sys


def left(dire):
    if dire is 0:
        dire += 3
    else:
        dire -= 1
    return dire


def right(dire):
    if dire is 3:
        dire -= 3
    else:
        dire += 1
    return dire


def move(num, x, y, dire):
    xx = dx[dire] + x
    yy = dy[dire] + y
    if xx >= a or xx < 0 or yy < 0 or yy >= b:
        print('Robot {} crashes into the wall'.format(num))
        exit()
    elif graph[yy][xx] is not 0:
        print('Robot {} crashes into robot {}'.format(num, graph[yy][xx]))
        exit()
    elif 0 <= xx < a and 0 <= yy < b:
        graph[y][x] = 0
        graph[yy][xx] = num
        robots[num - 1][0] = xx
        robots[num - 1][1] = yy


a, b = map(int,sys.stdin.readline().split())
graph = [[0 for j in range(a)] for i in range(b)]
n, m = map(int,sys.stdin.readline().split())
robots = [0 for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    x, y, z = sys.stdin.readline().split()
    x = int(x)
    y = int(y)
    if z is 'E':
        z = 0
    elif z is 'S':
        z = 1
    elif z is 'W':
        z = 2
    else:
        z = 3
    graph[b-y][x-1] = i + 1
    robots[i] = [x-1, b-y, z]

for _ in range(m):
    robot, command, cnt = sys.stdin.readline().split()
    robot = int(robot)
    cnt = int(cnt)
    for i in range(cnt):
        if command is 'L':
            robots[robot-1][2] = left(robots[robot-1][2])
        elif command is 'R':
            robots[robot-1][2] = right(robots[robot-1][2])
        else:
            move(robot, robots[robot-1][0], robots[robot-1][1], robots[robot-1][2])
print('OK')