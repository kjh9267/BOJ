# https://www.acmicpc.net/problem/2011

import sys
sys.setrecursionlimit(999999999)


def dfs(depth):
    if depth >= N:
        return 1
    if data[depth] == 0:
        return 0
    if dp[depth] != 0:
        return dp[depth]
    if data[depth] == 1:
        if depth != N - 1 and 1 <= data[depth + 1] <= 9:
            dp[depth] = dfs(depth + 1) + dfs(depth + 2)
        elif depth != N - 1 and data[depth + 1] == 0:
            dp[depth] = dfs(depth + 2)
        else:
            dp[depth] = dfs(depth + 1)
    elif data[depth] == 2:
        if depth != N - 1 and 1 <= data[depth + 1] <= 6:
            dp[depth] = dfs(depth + 1) + dfs(depth + 2)
        elif depth != N - 1 and data[depth + 1] == 0:
            dp[depth] = dfs(depth + 2)
        else:
            dp[depth] = dfs(depth + 1)
    else:
        dp[depth] = dfs(depth + 1)
    return dp[depth] % 1_000_000


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    data = list(map(int,input().rstrip()))
    N = len(data)
    dp = [0 for _ in range(N)]
    print(dfs(0))