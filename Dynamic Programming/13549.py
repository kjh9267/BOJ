# https://www.acmicpc.net/problem/13549

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, K = map(int,input().split())

    dp = [0 for _ in range(100001)]
    dp[N] = 0
    cnt = 1

    if N == K:
        print(0)
    else:
        for i in range(N - 1, -1, -1):
            dp[i] = cnt
            cnt += 1
        for i in range(N + 1, 100001):
            if i % 2 == 0:
                dp[i] = min(dp[i - 1] + 1, dp[i // 2])
            else:
                dp[i] = min(dp[i - 1] + 1, dp[(i + 1) // 2] + 1)
        print(dp[K])
