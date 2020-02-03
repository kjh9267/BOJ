# https://www.acmicpc.net/problem/1916

from sys import stdin
from queue import PriorityQueue


class Node:
    def __init__(self, node, cost):
        self.node = node
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def dijkstra():
    dist = [INF for _ in range(N + 1)]
    dist[start] = 0

    pq = PriorityQueue()
    pq.put(Node(start, 0))

    while not pq.empty():
        cur = pq.get()
        if dist[cur.node] < cur.cost:
            continue
        for nxt in graph[cur.node]:
            if dist[nxt.node] > dist[cur.node] + nxt.cost:
                dist[nxt.node] = dist[cur.node] + nxt.cost
                pq.put(Node(nxt.node, dist[nxt.node]))

    return dist


if __name__ == '__main__':
    input = stdin.readline
    N = int(input())
    M = int(input())
    INF = float('inf')
    graph = [list() for _ in range(N + 1)]

    for _ in range(M):
        cur, nxt, cost = map(int, input().split())
        graph[cur].append(Node(nxt, cost))

    start, end = map(int, input().split())
    dist = dijkstra()
    print(dist[end])