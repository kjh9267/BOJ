# https://www.acmicpc.net/problem/2234


def dfs(x, y, size):
    if visited[y][x]:
        return
    visited[y][x] = True
    size[A] += 1
    size_index[y][x] = A

    for idx, diff in enumerate(zip(dx, dy)):
        if (grid[y][x] & (1 << idx)) != 0:
            continue
        diff_x, diff_y = diff
        next_x = x + diff_x
        next_y = y + diff_y
        if next_x < 0 or next_x == M or next_y < 0 or next_y == N:
            continue
        dfs(next_x, next_y, size)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (-1, 0, 1, 0)
    dy = (0, -1, 0, 1)
    M, N = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    size_index = [[0 for _ in range(M)] for _ in range(N)]
    A, B, C = 0, 0, 0
    sizes = list()

    for row in range(N):
        for col in range(M):
            if visited[row][col]:
                continue
            sizes.append(0)
            dfs(col, row, sizes)
            B = max(B, sizes[A])
            A += 1

    for row in range(N):
        for col in range(M):
            for idx, diff in enumerate(zip(dx, dy)):
                if (grid[row][col] & (1 << idx)) == 0:
                    continue
                diff_x, diff_y = diff
                next_x = col + diff_x
                next_y = row + diff_y
                if next_x < 0 or next_x == M or next_y < 0 or next_y == N:
                    continue
                current_index = size_index[row][col]
                next_index = size_index[next_y][next_x]
                if current_index == next_index:
                    continue
                C = max(C, sizes[current_index] + sizes[next_index])

    print(A)
    print(B)
    print(C)