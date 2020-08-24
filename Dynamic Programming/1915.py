# https://www.acmicpc.net/problem/1915

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dx = (-1, 0, -1)
    dy = (0, -1, -1)
    N, M = map(int, input().split())
    grid = [list(map(int, input().rstrip())) for _ in range(N)]
    dp = [[0 for _ in range(M)] for _ in range(N)]
    result = 0

    for row in range(N):
        dp[row][0] = grid[row][0]
        result = max(result, dp[row][0])

    for col in range(M):
        dp[0][col] = grid[0][col]
        result = max(result, dp[0][col])

    for row in range(1, N):
        for col in range(1, M):
            if grid[row][col] == 0:
                continue
            dp[row][col] = min(dp[row - 1][col - 1], dp[row - 1][col], dp[row][col - 1]) + 1
            result = max(result, dp[row][col])

    print(result ** 2)