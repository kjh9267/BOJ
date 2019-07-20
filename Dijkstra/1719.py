# https://www.acmicpc.net/problem/1719

from queue import PriorityQueue
from sys import setrecursionlimit
setrecursionlimit(99999999)


class Node:
    def __init__(self, nxt, cost):
        self.nxt = nxt
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def dijkstra(start):
    pq = PriorityQueue()
    pq.put((0, start))
    dist = [inf for _ in range(N + 1)]
    dist[start] = 0
    while not pq.empty():
        cost, cur = pq.get()
        for n in graph[cur]:
            if dist[n.nxt] > dist[cur] + n.cost:
                dist[n.nxt] = dist[cur] + n.cost
                pq.put((dist[n.nxt], n.nxt))
                way[n.nxt] = cur


def dfs(cur, start, end):
    if way[cur] == start:
        res[start - 1][end - 1] = str(cur)
        return
    dfs(way[cur], start, end)


if __name__ =='__main__':
    input = __import__('sys').stdin.readline
    inf = float('inf')
    N, M = map(int,input().split())
    graph = [[] for _ in range(N + 1)]
    res = [['-' for col in range(N)] for row in range(N)]

    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append(Node(b, c))
        graph[b].append(Node(a, c))

    for start in range(1, N + 1):
        way = [-1 for _ in range(N + 1)]
        dijkstra(start)
        for end in range(1, N + 1):
            if start == end:
                continue
            dfs(end, start, end)

    for line in res:
        print(' '.join(line))