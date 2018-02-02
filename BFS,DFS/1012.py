import sys
from collections import deque # 파이썬에서 일반 list로 queue를 구현할 경우 pop할 때 O(1)이 아닌 O(n)이 걸리므로 deque사용


def bfs(node):
    queue = deque()
    queue.append(node)
    xx = [1, 0, -1, 0]
    yy = [0, 1, 0, -1]
    while queue:  # queue가 빌 때 까지 반복
        a = queue.popleft()
        visit[a[1]][a[0]] = 1
        # 인접 좌표에 배추가 있고, 아직 방문하지 않고, queue에 들어 있지 않을 때 queue에 append 해준다
        for i in range(4):
            dx = a[0] + xx[i]
            dy = a[1] + yy[i]
            if 0 <= dy < n and 0 <= dx < m:
                if graph[dy][dx] is 1 and visit[dy][dx] is 0 and [dx,dy] not in queue:
                    queue.append([dx,dy])


t = int(sys.stdin.readline()) # test케이스의 수
for _ in range(t):
    m, n, k = map(int,sys.stdin.readline().split())  # 가로길이, 세로길이, 배추의 수
    graph = [[0 for j in range(m)] for i in range(n)]
    visit = [[0 for j in range(m)] for i in range(n)]
    cnt = 0

    for i in range(k):
        x, y = map(int, sys.stdin.readline().split())
        graph[y][x] = 1
    for i in range(n):
        for j in range(m):
            if graph[i][j] is 1 and visit[i][j] is 0:   # 현재위치의 graph에 배추가 있고, 아직 방문하지 않은경우
                bfs([j,i])                              # bfs 탐색
                cnt += 1                                # bfs 탐색을 한 횟수
    print(cnt)