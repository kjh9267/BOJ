# https://www.acmicpc.net/problem/2823


def go(x, y):
    if grid[y][x] == 'X':
        return True
    wall_cnt = 0
    for i, j in zip(dx, dy):
        xx = x + i
        yy = y + j
        if not (0 <= xx < M and 0 <= yy < N):
            wall_cnt += 1
            continue
        if grid[yy][xx] == 'X':
            wall_cnt += 1
    if wall_cnt >= 3:
        return False
    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N , M = map(int,input().split())
    grid = [list(input().rstrip()) for _ in range(N)]
    dx = (0, 1, 0, -1)
    dy = (-1, 0, 1, 0)
    res = 0

    for row in range(N):
        for col in range(M):
            if not go(col, row):
                res = 1

    print(res)