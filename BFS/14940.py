# https://www.acmicpc.net/problem/14940


def bfs(x, y):
    queue = __import__('collections').deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for i, j in zip(dx, dy):
            xx = x + i
            yy = y + j
            if not(0 <= xx < M and 0 <= yy < N):
                continue
            if visited[yy][xx] != -1:
                continue
            if grid[yy][xx] == 0:
                continue
            queue.append((xx, yy))
            visited[yy][xx] = visited[y][x] + 1


if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0 , -1, 0)
    dy = (0, 1, 0 , -1)
    N , M = map(int, input().split())
    grid = [list(map(int,input().split())) for _ in range(N)]
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    x, y = 0, 0

    for row in range(N):
        for col in range(M):
            if grid[row][col] == 2:
                x, y = col, row
                visited[row][col] = 0
            elif grid[row][col] == 0:
                visited[row][col] = 0

    bfs(x, y)

    for row in visited:
        print(' '.join(map(str,row)))