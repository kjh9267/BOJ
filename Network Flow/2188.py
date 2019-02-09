#  https://www.acmicpc.net/problem/2188

from sys import stdin
from collections import deque


def matching(start,end):
    graph[start].append(end)
    graph[end].append(start)
    capacity[start].append(1)
    capacity[end].append(0)
    flow[start].append(0)
    flow[end].append(0)


def bfs():
    queue = deque()
    queue.append(0)
    way = [-1 for _ in range(sink+1)]
    while queue:
        cur = queue.popleft()
        for index, nxt in enumerate(graph[cur]):
            if capacity[cur][index] - flow[cur][index] > 0 and way[nxt] is -1:
                queue.append(nxt)
                way[nxt] = cur
                if nxt == sink:
                    return way
    return way


def solve():
    total = 0
    while True:
        way = bfs()
        if way[sink] is -1:
            break
        f = float('inf')
        cur = sink
        while cur is not 0:
            nxt = way[cur]
            index = graph[nxt].index(cur)
            if f > capacity[nxt][index] - flow[nxt][index]:
                f = capacity[nxt][index] - flow[nxt][index]
            cur = way[cur]
        cur = sink
        while cur is not 0:
            nxt = way[cur]
            flow[nxt][graph[nxt].index(cur)] += f
            flow[cur][graph[cur].index(nxt)] -= f
            cur = nxt
        total += f
    return total


if __name__ == '__main__':
    input = stdin.readline

    N, M = map(int,input().split())
    sink = N + M + 1
    graph = [[] for _ in range(sink + 1)]
    capacity = [[] for _ in range(sink + 1)]
    flow = [[] for _ in range(sink + 1)]

    for index in range(1,N+1):
        matching(0, index)

    for index in range(N+1,sink):
        matching(index, sink)

    for cur in range(1,N+1):
        nodes = list(map(int,input().split()))[1:]
        for nxt in nodes:
            matching(cur, N + nxt)

    print(solve())