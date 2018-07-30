# import sys
# from collections import deque
#
#
# def bfs():
#     queue = deque()
#     for i in range(m):
#         if not used[i]:
#             dist[i] = 0
#             queue.append(i)
#         else:
#             dist[i] = inf
#
#     while queue:
#         a = queue.popleft()
#         for b in range(graph[a][0],graph[a][1]):
#             print(b)
#             if B[b] is not -1 and dist[B[b]] is inf:
#                 dist[B[b]] = dist[a] + 1
#                 queue.append(B[b])
#
#
# def dfs(a):
#     for b in range(graph[a][0],graph[a][1]):
#         if B[b] is -1 or dist[B[b]] == dist[a] + 1 and dfs(B[b]):
#             used[a] = True
#             A[a] = b
#             B[b] = b
#             return True
#     return False
#
#
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     n, m = map(int,sys.stdin.readline().split())
#     A = [-1 for _ in range(m)]
#     B = [-1 for _ in range(n)]
#     graph = [[] for _ in range(m)]
#     inf = float('inf')
#     dist = [0 for _ in range(m)]
#     used = [False for _ in range(m)]
#     total = 0
#
#     for i in range(m):
#         a, b = map(int,sys.stdin.readline().split())
#         graph[i].extend([a-1,b])
#
#     while True:
#         bfs()
#         f = 0
#         for i in range(m):
#             if not used[i] and dfs(i):
#                 f += 1
#         if not f:
#             break
#         total += f
#
#     print(total)

import sys


def dfs(a):
    if visit[a]:
        return False
    visit[a] = 1
    for b in range(graph[a][0],graph[a][1]):
        if B[b] is -1 or visit[B[b]] is 0 and dfs(B[b]):
            A[a] = b
            B[b] = a
            return True
    return False


T = int(sys.stdin.readline())

for _ in range(T):
    n, m = map(int,sys.stdin.readline().split())
    A = [-1 for _ in range(m)]
    B = [-1 for _ in range(n)]
    graph = [[] for _ in range(m)]
    res = 0

    for i in range(m):
        a, b = map(int,sys.stdin.readline().split())
        graph[i].extend([a-1,b])

    for i in range(m):
        if A[i] is -1:
            visit = [0 for _ in range(m)]
            if dfs(i):
                res += 1

    print(res)