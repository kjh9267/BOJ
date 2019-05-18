# https://www.acmicpc.net/problem/17182


def floyd(start):
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    path[i][j][i] = True
                    path[i][j][k] = True
                    path[i][j][j] = True
                else:
                    path[i][j][i] = True
                    path[i][j][j] = True


def dijkstra(cur):
    res = 0
    while False in check:
        mini = float('inf')
        next = 0
        for nxt, cst in enumerate(graph[cur]):
            # print(visited, cur, nxt, cst)
            if mini >= cst and nxt != cur and not visited[cur][nxt]:
                mini = cst
                next -= next
                next += nxt
        visited[cur][next] = True
        res += mini
        for idx, boolean in enumerate(path[cur][next]):
            if boolean:
                check[idx] = True
        cur = next
    return res


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N, K = map(int,input().split())
    graph = [list(map(int,input().split())) for _ in range(N)]
    path = [[[False for _ in range(N)] for col in range(N)] for row in range(N)]
    visited = [[False for _ in range(N)] for i in range(N)]
    check = [False for _ in range(N)]
    check[K] = True
    dist = [float('inf') for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == j:
                visited[i][j] = True
    floyd(K)
    res = dijkstra(K)
    # print(graph)
    # for i in path:
    #     print(i)
    # print(check)
    print(res)