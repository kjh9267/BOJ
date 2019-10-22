# https://www.acmicpc.net/problem/17245

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    grid = [list(map(int,input().split())) for _ in range(N)]
    cnts = [0 for _ in range(10_000_001)]
    dp = [0 for _ in range(10_000_001)]
    full = 0

    for row in range(N):
        for col in range(N):
            value = grid[row][col]
            if value == 0:
                continue
            cnts[value] += 1
            full += value

    dp[10_000_000] = cnts[10_000_000]
    for idx in range(9_999_999, 0, -1):
        dp[idx] = dp[idx + 1] + cnts[idx]

    half = full / 2
    acc = 0
    for minute, cnt in enumerate(dp):
        acc += cnt
        if acc >= half:
            print(minute)
            break