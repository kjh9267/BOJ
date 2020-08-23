# https://www.acmicpc.net/problem/11779

from queue import PriorityQueue
from collections import deque


def dijkstra():
    pq = PriorityQueue()
    pq.put((0, start))

    dist = [inf for _ in range(N + 1)]
    dist[start] = 0

    while not pq.empty():
        _, cur = pq.get()
        for nxt, cost in graph[cur]:
            if dist[nxt] <= dist[cur] + cost:
                continue
            dist[nxt] = dist[cur] + cost
            pq.put((dist[nxt], nxt))
            way[nxt] = cur

    return dist


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    N = int(input())
    M = int(input())
    graph = [list() for _ in range(N + 1)]
    way = [0 for _ in range(N + 1)]
    result = deque()

    for _ in range(M):
        start, end, cost = map(int, input().split())
        graph[start].append((end, cost))

    start, end = map(int, input().split())
    dist = dijkstra()
    result.append(end)
    node = end

    while node != start:
        result.appendleft(way[node])
        node = way[node]

    print(dist[end])
    print(len(result))
    print(' '.join(map(str, result)))