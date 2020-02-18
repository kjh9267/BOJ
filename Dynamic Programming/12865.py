# https://www.acmicpc.net/problem/12865

import sys
sys.setrecursionlimit(999999999)


def dfs(cur, total):
    if cur == N:
        return 0
    if dp[cur][total] != -1:
        return dp[cur][total]
    dp[cur][total] = 0
    dp[cur][total] = max(dp[cur][total], dfs(cur + 1, total))
    if total + weights[cur] > K:
        return dp[cur][total]
    dp[cur][total] = max(dp[cur][total], dfs(cur + 1, total + weights[cur]) + values[cur])
    return dp[cur][total]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, K = map(int, input().split())
    weights = [0 for _ in range(N)]
    values = [0 for _ in range(N)]
    dp = [[-1 for _ in range(K + 1)] for _ in range(N)]

    for idx in range(N):
        w, v = map(int, input().split())
        weights[idx] = w
        values[idx] = v

    print(dfs(0, 0))