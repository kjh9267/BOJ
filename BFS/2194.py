# https://www.acmicpc.net/problem/2194


def bfs():
    queue = __import__('collections').deque()
    queue.append((start_x, start_y))

    visited = [[-1 for _ in range(M)] for _ in range(N)]
    visited[start_y][start_x] = 0

    while queue:
        x, y = queue.popleft()
        for diff_x, diff_y in zip(dx, dy):
            next_x = x + diff_x
            next_y = y + diff_y
            if not (0 <= next_x <= M - B and 0 <= next_y <= N - A):
                continue
            if not can_go(next_x, next_y):
                continue
            if visited[next_y][next_x] != -1:
                continue
            queue.append((next_x, next_y))
            visited[next_y][next_x] = visited[y][x] + 1

    return visited[end_y][end_x]


def can_go(x, y):
    for row in range(y, y + A):
        for col in range(x, x + B):
            if grid[row][col]:
                return False
    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    N, M, A, B, K = map(int, input().split())
    grid = [[False for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        row, col = map(lambda x: int(x) - 1, input().split())
        grid[row][col] = True

    start_y, start_x = map(lambda x: int(x) - 1, input().split())
    end_y, end_x = map(lambda x: int(x) - 1, input().split())

    print(bfs())