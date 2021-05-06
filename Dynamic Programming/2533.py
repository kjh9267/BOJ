# https://www.acmicpc.net/problem/2533

import sys
sys.setrecursionlimit(999999999)


def init_tree(cur):
    for nxt in tree[cur]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        init_tree(nxt)
        new_tree[cur].append(nxt)


def dfs(cur, is_adapter):
    is_leaf = cur != root and len(new_tree[cur]) == 0

    if is_leaf:
        return is_adapter

    if dp[cur][is_adapter] != -1:
        return dp[cur][is_adapter]

    dp[cur][is_adapter] = is_adapter
    for nxt in new_tree[cur]:
        if is_adapter == 0:
            dp[cur][is_adapter] += dfs(nxt, 1)
        else:
            dp[cur][is_adapter] += min(dfs(nxt, 0), dfs(nxt, 1))

    return dp[cur][is_adapter]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    root = 1
    N = int(input())
    tree = [list() for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    new_tree = [list() for _ in range(N + 1)]
    dp = [[-1 for _ in range(2)] for _ in range(N + 1)]

    for _ in range(N - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)

    visited[root] = True
    init_tree(root)
    tree.clear()
    visited.clear()

    print(min(dfs(root, 1), dfs(root, 0)))
