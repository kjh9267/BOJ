import sys

graph = [[0 for __ in range(6)] for _ in range(6)]
visit = [[0 for __ in range(6)] for _ in range(6)]
dx = (1,1,-1,-1,2,2,-2,-2)
dy = (2,-2,2,-2,1,-1,1,-1)

xx, yy = sys.stdin.readline().rstrip()
xx = ord(xx) - 65
yy = int(yy) - 1
visit[yy][xx] = 1
start = (xx,yy)

for i in range(35):
    key = False
    x, y = sys.stdin.readline().rstrip()
    x = ord(x) - 65
    y = int(y) - 1
    if visit[y][x] is 0:
        for j, u in zip(dx,dy):
            if xx + j == x and yy + u == y:
                visit[y][x] = 1
    xx, yy = x, y
    if i == 34 and sum([sum(i) for i in visit]) == 36:
        for j, u in zip(dx,dy):
            if xx + j == start[0] and yy + u == start[1]:
                key = True

if key is False:
    print('Invalid')
else:
    print('Valid')