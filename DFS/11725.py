#  https://www.acmicpc.net/problem/11725

import sys


def dfs(cur):
    if visited[cur]:
        return
    visited[cur] = True
    for nxt in tree[cur]:
        dfs(nxt)
        parent[nxt] = cur


if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    input = __import__('sys').stdin.readline

    N = int(input())
    tree = [[] for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    parent = [0 for _ in range(N + 1)]

    for _ in range(N - 1):
        A, B = map(int,input().split())
        tree[A].append(B)
        tree[B].append(A)

    dfs(1)

    for p in parent[2:]:
        print(p)