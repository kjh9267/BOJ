import sys
from collections import deque


def dfs(x,y,cnt):
    visit[y][x] = 1
    for i, j in zip(dx,dy):
        xx = x + i
        yy = y + j
        if 0 <= xx < 6 and 0 <= yy < 12:
            if graph[yy][xx] == graph[y][x] and visit[yy][xx] == 0:
                cnt = dfs(xx,yy, cnt + 1)
    return cnt


def delete(x,y):
    color = graph[y][x]
    queue = deque()
    queue.append((x,y))
    visit[y][x] = 2
    graph[y][x] = '.'
    while queue:
        a = queue.popleft()
        for i, j in zip(dx,dy):
            xx = i + a[0]
            yy = j + a[1]
            if 0 <= xx < 6 and 0 <= yy < 12:
                if graph[yy][xx] == color and visit[yy][xx] == 1:
                    graph[yy][xx] = '.'
                    queue.append((xx,yy))
                    visit[yy][xx] = 2


def down(x,y):
    color = graph[y][x]             # 블럭 색깔
    for i in range(y,11):           # 블럭 위치부터 밑에서 두번째 줄 까지
        if graph[i+1][x] == '.':    # 다음 줄이 빈공간 이면
            graph[i][x] = '.'       # 현재 비우고
            graph[i+1][x] = color   # 다음줄 블럭으로 채우고
        elif graph[i+1][x] != '.':  # 다음줄 블럭이면 끝
            break


graph = [list(sys.stdin.readline().rstrip()) for _ in range(12)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
change = True
result = 0

while change:
    change = False
    visit = [[0 for j in range(6)] for i in range(12)]

    for i in range(12):
        for j in range(6):
            if graph[i][j] != '.' and visit[i][j] == 0:
                if dfs(j,i,1) >= 4:
                    delete(j,i)
                    change = True

    for i in range(10,-1,-1):       # 밑에서 두번째 줄 부터 검사
        for j in range(6):
            if graph[i][j] != '.':  # 빈공간이 아니면 ( 블럭이면 )
                down(j,i)           # 떨구는 함수 호출

    if change:
        result += 1

print(result)