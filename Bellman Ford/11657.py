#  https://www.acmicpc.net/problem/11657

import sys


class Node:
    def __init__(self, nxt, cost):
        self.nxt = nxt
        self.cost = cost


if __name__ == '__main__':
    input = sys.stdin.readline

    N, M = map(int,input().split())
    graph = [[] for _ in range(N)]
    inf = float('inf')
    res = [inf for _ in range(N)]
    res[0] = 0

    for _ in range(M):
        a, b, c = map(int,input().split())
        graph[a-1].append(Node(b-1, c))

    for i in range(N):
        for j in range(N):
            for node in graph[j]:
                if res[j] != inf and res[node.nxt] > res[j] + node.cost:
                    res[node.nxt] = res[j] + node.cost
                    if i == N - 1:
                        print(-1)
                        exit()

    for i in range(1,N):
        if res[i] == inf:
            print(-1)
        else:
            print(res[i])