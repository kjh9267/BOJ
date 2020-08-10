# https://www.acmicpc.net/problem/2533
import sys
sys.setrecursionlimit(999999999)


def dfs(cur, color, prev_color):
    if dp[cur][color] != -1:
        return dp[cur][color]

    dp[cur][color] = color

    temp = 0
    for nxt in tree[cur]:
        if not (prev_color == color == 0):
            ret = dfs(nxt, 0, color)
            temp = max(temp, ret)
        ret = dfs(nxt, 1, color)
        temp = max(temp, ret)

    dp[cur][color] += temp

    return dp[cur][color]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    N = int(input())
    tree = [list() for _ in range(N + 1)]
    dp = [[-1 for _ in range(2)] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    print(dfs(1, 0, 0))
    print(dp)
    print(dfs(1, 1, 0))
    print(dp)