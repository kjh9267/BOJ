# https://www.acmicpc.net/problem/2251

import sys
sys.setrecursionlimit(99999999)


class Node:
    def __init__(self, capacity, nxt):
        self.capacity = capacity
        self.nxt = nxt


def dfs(cur, waters):
    check = cur * 1_000_000_000 + waters[0] * 1_000_000 + waters[1] * 1_000 + waters[2]
    if check in visited:
        return
    visited.add(check)
    if waters[0] == 0:
        res.add(waters[2])

    for node in graph[cur]:
        other = 3 - cur - node.nxt
        next_water = [0 for _ in range(3)]
        sumi = waters[cur] + waters[node.nxt]
        next_water[cur] = sumi - node.capacity if sumi > node.capacity else 0
        next_water[node.nxt] = sumi if sumi <= node.capacity else node.capacity
        next_water[other] = waters[other]
        dfs(node.nxt, next_water)
        sumi = next_water[cur] + waters[other]
        nxt_capacity = capacities[other]
        next_water[other] = sumi if sumi <= nxt_capacity else nxt_capacity
        next_water[cur] = sumi - nxt_capacity if sumi > nxt_capacity else 0
        dfs(node.nxt, next_water)
        dfs(node.nxt, waters)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    capacities = list(map(int,input().split()))
    graph = [list() for _ in range(3)]
    graph[0].append(Node(capacities[1], 1))
    graph[0].append(Node(capacities[2], 2))
    graph[1].append(Node(capacities[0], 0))
    graph[1].append(Node(capacities[2], 2))
    graph[2].append(Node(capacities[0], 0))
    graph[2].append(Node(capacities[1], 1))

    res = set()
    visited = set()
    dfs(2, [0, 0, capacities[2]])
    print(' '.join(map(str,sorted(list(res)))))
