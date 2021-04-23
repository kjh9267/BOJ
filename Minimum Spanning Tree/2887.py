# https://www.acmicpc.net/problem/2887

from queue import PriorityQueue


class Node:
    def __init__(self, cur, nxt, cost):
        self.cur = cur
        self.nxt = nxt
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost


def insert_nodes(sorted_nodes, point):
    for index in range(N - 1):
        cur = sorted_nodes[index][3]
        nxt = sorted_nodes[index + 1][3]
        cost = abs(sorted_nodes[index][point] - sorted_nodes[index + 1][point])
        pq.put(Node(cur, nxt, cost))


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
    count = 0
    minimum_cost = 0

    while not pq.empty():
        node = pq.get()
        if merge(node.cur, node.nxt):
            minimum_cost += node.cost
            count += 1
            if count == N - 1:
                break

    return minimum_cost


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    N = int(input())
    parent = [-1 for _ in range(N)]
    nodes = [list(map(int, input().split())) + [node_num] for node_num in range(N)]
    sorted_by_x = sorted(nodes, key=lambda x: x[0])
    sorted_by_y = sorted(nodes, key=lambda x: x[1])
    sorted_by_z = sorted(nodes, key=lambda x: x[2])
    pq = PriorityQueue()

    insert_nodes(sorted_by_x, 0)
    insert_nodes(sorted_by_y, 1)
    insert_nodes(sorted_by_z, 2)



    print(mst())

