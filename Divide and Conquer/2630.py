# https://www.acmicpc.net/problem/2630


def solve(x, y, size):
    global white, blue
    cnt = 0
    for i in range(y, y + size):
        for j in range(x, x + size):
            cnt += grid[i][j]
    if cnt == size ** 2:
        blue += 1
        return
    elif cnt == 0:
        white += 1
        return

    half = size // 2
    solve(x, y, half)
    solve(x + half, y, half)
    solve(x, y + half, half)
    solve(x + half, y + half, half)


if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    white = 0
    blue = 0
    solve(0, 0, N)
    print(white)
    print(blue)