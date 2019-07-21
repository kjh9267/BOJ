# https://www.acmicpc.net/problem/12849

import sys
sys.setrecursionlimit(999999999)


def solve(cur, time):
    if time == D:
        return 1 if cur == 0 else 0
    if dp[cur][time] != 0:
        return dp[cur][time] % MOD
    for nxt in graph[cur]:
        dp[cur][time] = ((dp[cur][time] % MOD) + (solve(nxt, time + 1) % MOD)) % MOD
    return dp[cur][time] % MOD


def init():
    graph[0].append(1)
    graph[1].append(0)
    graph[0].append(2)
    graph[2].append(0)
    graph[2].append(1)
    graph[1].append(2)
    graph[2].append(3)
    graph[3].append(2)
    graph[2].append(4)
    graph[4].append(2)
    graph[3].append(1)
    graph[1].append(3)
    graph[4].append(3)
    graph[3].append(4)
    graph[5].append(3)
    graph[3].append(5)
    graph[4].append(5)
    graph[5].append(4)
    graph[4].append(6)
    graph[6].append(4)
    graph[5].append(7)
    graph[7].append(5)
    graph[6].append(7)
    graph[7].append(6)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    MOD = 1_000_000_007
    D = int(input())
    dp = [[0 for _ in range(100_001)] for __ in range(8)]
    graph = [[] for _ in range(8)]
    init()
    print(solve(0, 0))
