# https://www.acmicpc.net/problem/11438


def dfs(cur):
    for idx, nxt in enumerate(adj):
        if parent[nxt][0] == -1:
            parent[nxt][0] = cur
            depth[nxt] = depth[cur] + 1
            dfs(nxt)


def fill_parent():
    for p in range(H):
        for idx in range(1, N):
            if parent[idx][p] == -1:
                continue
            parent[idx][p + 1] = parent[parent[idx][p]][p]


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    H = 1

    while H < N:
        H <<= 1

    adj = [list() for _ in range(N)]
    parent = [[-1 for _ in range(H)] for _ in range(N)]
    depth = [-1 for _ in range(N)]
    depth[0] = 0

    for _ in range(N):
        u, v = map(lambda x: int(x) - 1, input().split())
        adj[u].append(v)
        adj[v].append(u)

    dfs(0)
    fill_parent()
    M = int(input())

    for _ in range(M):
        u, v = map(lambda x: int(x) - 1, input().split())
