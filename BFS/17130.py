# https://www.acmicpc.net/problem/17130


def bfs(x, y):
    queue = __import__('collections').deque()
    queue.append((x, y))
    dist[y][x] = 0

    while queue:
        x, y = queue.popleft()
        for idx, diff in enumerate(zip(dx, dy)):
            diff_x, diff_y = diff
            next_x = x + diff_x
            next_y = y + diff_y
            if not(0 <= next_y < N and 0 <= next_x < M):
                continue
            plus = 1 if grid[next_y][next_x] == 'C' else 0
            if dist[next_y][next_x] >= dist[y][x] + plus:
                continue
            if grid[next_y][next_x] == '#':
                continue
            dist[next_y][next_x] = dist[y][x] + plus
            queue.append((next_x, next_y))


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 1, 1)
    dy = (-1, 0, 1)
    N, M = map(int, input().split())
    grid = [input().rstrip() for _ in range(N)]
    dist = [[-1 for _ in range(M)] for _ in range(N)]

    for row in range(N):
        for col in range(M):
            if grid[row][col] == 'R':
                bfs(col, row)

    res = -1
    for row in range(N):
        for col in range(M):
            if grid[row][col] != 'O':
                continue
            res = max(res, dist[row][col])

    print(res)