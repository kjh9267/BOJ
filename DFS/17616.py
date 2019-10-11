# https://www.acmicpc.net/problem/17616


def dfs(cur, adj, depth):
    global L, R
    if visited[cur]:
        return
    visited[cur] = True
    for nxt in adj[cur]:
        dfs(nxt, adj, depth + 1)
    if adj is front:
        L += 1
    else:
        R += 1


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N, M, X = map(int,input().split())
    front = [list() for _ in range(N)]
    back = [list() for _ in range(N)]
    visited = [False for _ in range(N)]
    L = -1
    R = -1

    for _ in range(M):
        a, b = map(lambda x: int(x) - 1, input().split())
        back[a].append(b)
        front[b].append(a)

    dfs(X - 1, front, 0)
    visited = [False for _ in range(N)]
    dfs(X - 1, back, 0)
    print(1 + L, N - R)