#  https://www.acmicpc.net/problem/11375


def dfs(cur):
    if visited[cur]:
        return False
    visited[cur] = True
    for nxt in graph[cur]:
        if B[nxt] == -1 or dfs(B[nxt]):
            A[cur] = nxt
            B[nxt] = cur
            return True
    return False


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N, M = map(int,input().split())
    graph = [[] for _ in range(N)]
    A = [-1 for _ in range(N)]
    B = [-1 for _ in range(M)]
    res = 0

    for index in range(N):
        data = list(map(lambda x: int(x) - 1,input().split()))[1:]
        graph[index].extend(data)

    for index in range(N):
        if A[index] != -1:
            continue
        visited = [False for _ in range(N)]
        if dfs(index):
            res += 1

    print(res)
