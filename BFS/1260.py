# https://www.acmicpc.net/problem/1260


def dfs(cur, path):
    if visited[cur]:
        return path
    visited[cur] = True
    path += str(cur) + _space
    for nxt in adj[cur]:
        path = dfs(nxt, path)
    return path


def bfs(start):
    queue = __import__('collections').deque()
    queue.append(start)
    visited[start] = True
    path = ''

    while queue:
        cur = queue.popleft()
        path += str(cur) + _space
        for nxt in adj[cur]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append(nxt)

    return path


if __name__ == '__main__':
    _space = ' '
    input = __import__('sys').stdin.readline
    N, M, V = map(int, input().split())
    adj = [list() for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]

    for _ in range(M):
        x, y = map(int, input().split())
        adj[x].append(y)
        adj[y].append(x)

    for idx in range(1, N + 1):
        adj[idx].sort()

    print(dfs(V, ''))
    visited = [False for _ in range(N + 1)]
    print(bfs(V))
