# https://www.acmicpc.net/problem/1347

if __name__ =='__main__':
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    input = __import__('sys').stdin.readline
    N = int(input())
    data = list(input().rstrip())
    grid = [['#' for _ in range(110)] for _ in range(111)]
    grid[55][55] = '.'
    row_start, row_end, col_start, col_end = 55, 55, 55, 55
    x, y, idx = 55, 55, 2

    for op in data:
        if op == 'R':
            idx = (idx + 1) % 4
        elif op == 'L':
            idx = idx - 1 if idx != 0 else 3
        else:
            ny, nx = y + dy[idx], x + dx[idx]
            grid[ny][nx] = '.'
            row_start = min(row_start, ny)
            row_end = max(row_end, ny)
            col_start = min(col_start, nx)
            col_end = max(col_end, nx)
            x, y = nx, ny

    for row in range(row_start, row_end + 1):
        print(''.join(grid[row][col_start: col_end + 1]))