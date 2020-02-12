# https://www.acmicpc.net/problem/1149

import sys
sys.setrecursionlimit(999999999)


def dfs(home, color):
    if home == N - 1:
        return data[home][color]
    if dp[home][color] != inf:
        return dp[home][color]
    for num in range(3):
        if num == color:
            continue
        dp[home][color] = min(dp[home][color], dfs(home + 1, num) + data[home][color])
    return dp[home][color]


def dfs_all():
    res = inf
    for color in range(3):
        res = min(res,dfs(0, color))
    return res


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    dp = [[inf for _ in range(3)] for _ in range(N)]
    print(dfs_all())