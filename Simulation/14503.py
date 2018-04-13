import sys


def change():
    if robot[2] is 0:
        robot[2] = 3
    else:
        robot[2] -= 1


def check():
    xx = robot[1] + dx[robot[2]]
    yy = robot[0] + dy[robot[2]]
    if 0 <= xx < m and 0 <= yy < n:
        if graph[yy][xx] is 0 and visit[yy][xx] is 0:
            return True
    else:
        return False


def move():
    global cnt
    for _ in range(4):
        change()
        if check():
            robot[1] += dx[robot[2]]
            robot[0] += dy[robot[2]]
            visit[robot[0]][robot[1]] = 1
            cnt += 1
            break
    else:
        change()
        change()
        robot[1] += dx[robot[2]]
        robot[0] += dy[robot[2]]
        if 0 <= robot[1] < m and 0 <= robot[0] < n and graph[robot[0]][robot[1]] is 0:
            change()
            change()
        else:
            print(cnt)
            exit()


n, m = map(int,sys.stdin.readline().split())
robot = list(map(int,sys.stdin.readline().split()))
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
visit = [[0 for __ in range(m)] for _ in range(n)]
visit[robot[0]][robot[1]] = 1
dx = (0,1,0,-1)
dy = (-1,0,1,0)
cnt = 1

while True:
    move()