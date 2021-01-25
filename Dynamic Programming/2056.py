# https://www.acmicpc.net/problem/2056
import sys
sys.setrecursionlimit(999999999)


def dfs_all():
    result = 0

    for work, prev_works in enumerate(data):
        if len(prev_works[2:]) == 0:
            result = max(result, dfs(work))

    return result


def dfs(current_work):
    if dp[current_work] != 0:
        return dp[current_work]

    for next_work in adj[current_work]:
        dp[current_work] = max(dp[current_work], dfs(next_work) + need_times[current_work])

    if dp[current_work] == 0:
        dp[current_work] = need_times[current_work]

    return dp[current_work]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]
    need_times = [data[work][0] for work in range(N)]
    adj = [list() for work in range(N)]
    dp = [0 for _ in range(N)]

    for work, prev_works in enumerate(data):
        for prev_work in prev_works[2:]:
            adj[prev_work - 1].append(work)

    print(dfs_all())