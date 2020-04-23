# https://www.acmicpc.net/problem/9084
import sys
sys.setrecursionlimit(999999999)


def dfs(depth, coin):
    if depth > M:
        return 0
    if depth == M:
        return 1
    if dp[depth][coin] != -1:
        return dp[depth][coin]

    dp[depth][coin] = 0
    for idx in range(coin, N):
        dp[depth][coin] += dfs(depth + data[idx], idx)

    return dp[depth][coin]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    T = int(input())

    for _ in range(T):
        N = int(input())
        data = list(map(int, input().split()))
        M = int(input())
        dp = [[-1 for _ in range(N)] for _ in range(M)]
        print(dfs(0, 0))