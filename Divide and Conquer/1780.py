# https://www.acmicpc.net/problem/1780
import sys
sys.setrecursionlimit(999999999)


def solve(x, y, size):
    for target in range(-1, 2):
        if check(x, y, size, target):
            result[target + 1] += 1
            return

    size //= 3
    diff = (0, size, size * 2)

    for diff_x in diff:
        for diff_y in diff:
            solve(x + diff_x, y + diff_y, size)


def check(x, y, size, target):

    for row in range(y, y + size):
        for col in range(x, x + size):
            if grid[row][col] != target:
                return False
    return True


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    grid = [list(map(int, input().split())) for _ in range(N)]
    result = [0, 0, 0]

    solve(0, 0, N)

    for value in result:
        print(value)