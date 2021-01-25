# https://www.acmicpc.net/problem/13023

import sys
sys.setrecursionlimit(999999999)


def dfs_all():
    is_possible = [False]

    for node in range(N):
        visited = [False for _ in range(N)]
        dfs(node, 0, visited, is_possible)

        if is_possible[0]:
            return 1

    return 0


def dfs(cur, depth, visited, is_possible):
    if visited[cur]:
        return

    if depth == target_depth:
        is_possible[0] = True
        return
    visited[cur] = True

    for nxt in graph[cur]:
        dfs(nxt, depth + 1, visited, is_possible)

    visited[cur] = False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    target_depth = 4
    N, M = map(int, input().split())
    graph = [list() for _ in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print(dfs_all())
