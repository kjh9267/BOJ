# https://www.acmicpc.net/problem/15705


def solve():
    for row in range(N):
        for col in range(M):
            for idx in range(8):
                if dfs(col, row, idx, 0):
                    return 1
    return 0


def dfs(x, y, idx, pointer):
    if pointer == len(word):
        return True
    if not (0 <= x < M and 0 <= y < N):
        return False
    if grid[y][x] == word[pointer]:
        return dfs(x + dx[idx], y + dy[idx], idx, pointer + 1)
    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (1, 0, -1, 0, 1, 1, -1, -1)
    dy = (0, 1, 0, -1, 1, -1, 1, -1)
    word = input().rstrip()
    N, M = map(int,input().split())
    grid = [input().rstrip() for _ in range(N)]
    print(solve())