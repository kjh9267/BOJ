# https://www.acmicpc.net/problem/1938


def bfs():
    queue = __import__('collections').deque()
    visited = [[[-1 for _ in range(2)] for _ in range(N)] for _ in range(N)]

    queue.append((start_x, start_y, start_vertical))
    visited[start_y][start_x][start_vertical] = 0

    while queue:
        x, y, v = queue.popleft()
        for diff_x, diff_y in zip(dx, dy):
            next_x = x + diff_x
            next_y = y + diff_y
            if not (0 <= next_x < N and 0 <= next_y < N):
                continue
            if not can_go(next_x, next_y, v):
                continue
            if visited[next_y][next_x][v] != -1:
                continue
            visited[next_y][next_x][v] = visited[y][x][v] + 1
            queue.append((next_x, next_y, v))

        if not can_rotate(x, y):
            continue

        if v == 1 and visited[y][x][0] == -1:
            visited[y][x][0] = visited[y][x][1] + 1
            queue.append((x, y, 0))
        elif visited[y][x][1] == -1:
            visited[y][x][1] = visited[y][x][0] + 1
            queue.append((x, y, 1))

    return visited


def can_go(x, y, v):
    if v == 1:
        for diff_y in range(-1, 2):
            next_y = y + diff_y
            if not (0 <= next_y < N):
                return False
            if grid[next_y][x] == '1':
                return False
    else:
        for diff_x in range(-1, 2):
            next_x = x + diff_x
            if not (0 <= next_x < N):
                return False
            if grid[y][next_x] == '1':
                return False
    return True


def can_rotate(x, y):
    for diff_x in range(-1, 2):
        for diff_y in range(-1, 2):
            next_x = x + diff_x
            next_y = y + diff_y
            if not (0 <= next_y < N and 0 <= next_x < N):
                return False
            if grid[next_y][next_x] == '1':
                return False
    return True


if __name__ == '__main__':
    dx = (1, 0, -1, 0)
    dy = (0, 1, 0, -1)
    input = __import__('sys').stdin.readline
    N = int(input())
    grid = [input().rstrip() for _ in range(N)]
    start_x, start_y, start_vertical = -1, -1, 0
    end_x, end_y, end_vertical = -1, -1, 0

    for row in range(N):
        for col in range(N):
            if grid[row][col] == 'B':
                start_x += col
                start_y += row
                if row + 1 < N and grid[row + 1][col] == 'B':
                    start_vertical = 1
            elif grid[row][col] == 'E':
                end_x += col
                end_y += row
                if row + 1 < N and grid[row + 1][col] == 'E':
                    end_vertical = 1

    start_x = (start_x + 3) // 3
    start_y = (start_y + 3) // 3
    end_x = (end_x + 3) // 3
    end_y = (end_y + 3) // 3

    res = bfs()[end_y][end_x][end_vertical]

    print(res if res != -1 else 0)
