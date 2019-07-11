# https://www.acmicpc.net/problem/10870

import sys
sys.setrecursionlimit(99999999)


def solve(cur):
    if cur == 0:
        return 0
    if cur == 1:
        return 1
    if dp[cur] != -1:
        return dp[cur]
    dp[cur] = solve(cur - 1) + solve(cur - 2)
    return dp[cur]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    dp = [-1 for _ in range(10_001)]
    n = int(input())
    print(solve(n))
