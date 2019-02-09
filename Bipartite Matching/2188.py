#  https://www.acmicpc.net/problem/2188


def dfs(cur):
    if visit[cur]:
        return False
    visit[cur] = True
    for nxt in graph[cur]:
        if B[nxt] is -1 or dfs(B[nxt]):
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
    cnt = 0

    for cur in range(N):
        nodes = list(map(int,input().split()))[1:]
        for nxt in nodes:
            graph[cur].append(nxt - 1)

    for index in range(N):
        if A[index] is -1:
            visit = [False for _ in range(N)]
            if dfs(index):
                cnt += 1
    print(cnt)