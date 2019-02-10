#  https://www.acmicpc.net/problem/11408

import sys
from collections import deque


def match(u,v,c):
    graph[u].append(v)
    graph[v].append(u)
    cost[u][v] = c
    cost[v][u] = -c
    capacity[u][v] = 1


def spfa():
    queue = deque()
    queue.append(0)
    way = [-1 for _ in range(sink)]
    dist = [inf for _ in range(sink)]
    inQ = [False for _ in range(sink)]
    inQ[0] = True
    dist[0] = 0
    while queue:
        cur = queue.popleft()
        inQ[cur] = False
        for nxt in graph[cur]:
            if capacity[cur][nxt] - flow[cur][nxt] > 0 and dist[nxt] > dist[cur] + cost[cur][nxt]:
                dist[nxt] = dist[cur] + cost[cur][nxt]
                way[nxt] = cur
                if not inQ[nxt]:
                    queue.append(nxt)
                    inQ[nxt] = True
    return way


def solve():
    total = 0
    cnt = 0
    while True:
        way = spfa()
        if way[sink-1] is -1:
            break
        cur = sink - 1
        while cur is not 0:
            nxt = way[cur]
            total += cost[nxt][cur]
            flow[nxt][cur] += 1
            flow[cur][nxt] -= 1
            cur = nxt
        cnt += 1
    return cnt, total


if __name__ == '__main__':
    N, M = map(int,sys.stdin.readline().split())
    inf = float('inf')
    sink = N + M + 2
    graph = [[] for _ in range(sink)]
    capacity = [[0 for col in range(sink)] for row in range(sink)]
    flow = [[0 for col in range(sink)] for row in range(sink)]
    cost = [[0 for col in range(sink)] for row in range(sink)]

    for person in range(1,N+1):
        data = list(map(int,sys.stdin.readline().split()))

        for index in range(1, data[0] * 2 + 1, 2):
            match(person, data[index] + N, data[index + 1])

    for index in range(1, N + 1):
        match(0, index, 0)

    for index in range(N + 1, sink - 1):
        match(index, sink - 1, 0)

    print('\n'.join(map(str,solve())))