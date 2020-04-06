# https://www.acmicpc.net/problem/11054
import sys
sys.setrecursionlimit(999999999)


def dfs(cur, direction, maxi, mini):

    max_num = max(maxi, data[cur])
    min_num = min(mini, data[cur]) if direction == 1 and cur != 0 else mini
    num = max_num if direction == 0 else min_num

    if dp[cur][direction][num] != -1:
        return dp[cur][direction][num]

    dp[cur][direction][num] = 0
    for nxt in range(cur + 1, N + 1):
        if data[nxt] == data[cur]:
            continue
        if direction == 0 and data[nxt] > max_num:
            dp[cur][direction][num] = max(dp[cur][direction][num], dfs(nxt, 0, max_num, min_num) + 1)
        if data[nxt] < min_num:
            dp[cur][direction][num] = max(dp[cur][direction][num], dfs(nxt, 1, max_num, min_num) + 1)

    return dp[cur][direction][num]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    data = [0] + list(map(int, input().split()))
    dp = [[[-1 for _ in range(1_001)] for _ in range(2)] for _ in range(N + 1)]
    print(dfs(0, 0, 0, float('inf')))