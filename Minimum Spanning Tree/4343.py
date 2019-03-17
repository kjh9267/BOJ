#  https://www.acmicpc.net/problem/4343

from queue import PriorityQueue
from math import sqrt


def find(x):
    if parent[x] < 0:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def merge(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return False
    if parent[x] > parent[y]:
        parent[y] += parent[x]
        parent[x] = y
    else:
        parent[x] += parent[y]
        parent[y] = x
    return True


def mst():
    res = 0
    cnt = 0

    while not pq.empty():
        cost, n1, n2 = pq.get()
        if merge(n1, n2):
            res = max(res, cost)
            cnt += 1
            if cnt == target:
                break

    return res


class Node:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y


if __name__ == '__main__':
    input = __import__('sys').stdin.readline

    N = int(input())

    for _ in range(N):
        S, P = map(int,input().split())
        parent = [-1 for _ in range(P)]
        pq = PriorityQueue()
        nodes = list()
        s_link = S - 1
        target = P - 1 - s_link

        for num in range(P):
            x, y = map(int,input().split())
            nodes.append(Node(num, x, y))

        for idx1 in range(P):
            for idx2 in range(idx1 + 1, P):
                n1 = nodes[idx1]
                n2 = nodes[idx2]
                cost = sqrt((n1.x - n2.x) ** 2 + (n1.y - n2.y) ** 2)
                pq.put((cost, n1.num, n2.num))
        print("{:.2f}".format(mst()))