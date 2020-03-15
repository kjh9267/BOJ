# https://www.acmicpc.net/problem/2579

import sys
sys.setrecursionlimit(999999999)


def dfs(cur, adj_cnt):
    if cur > N:
        return -inf
    if cur == N:
        return data[cur]
    if dp[cur][adj_cnt] != 0:
        return dp[cur][adj_cnt]
    dp[cur][adj_cnt] = max(dp[cur][adj_cnt], dfs(cur + 2, 1) + data[cur])
    if adj_cnt < 2:
        dp[cur][adj_cnt] = max(dp[cur][adj_cnt], dfs(cur + 1, adj_cnt + 1) + data[cur])
    return dp[cur][adj_cnt]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    N = int(input())
    data = [0 for _ in range(N + 1)]
    dp = [[0 for _ in range(3)] for _ in range(N + 1)]

    for idx in range(1, N + 1):
        data[idx] = int(input())

    print(dfs(0, 0))