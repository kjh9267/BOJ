# https://www.acmicpc.net/problem/4650


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
    cnt = 0
    min_cost = 0
    while not pq.empty():
        c, a, b = pq.get()
        if merge(a, b):
            min_cost += c
            cnt += 1
            if cnt == N - 1:
                break
    return min_cost


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    M = int(input())

    while M != 0:
        pq = __import__('queue').PriorityQueue()
        parent = [-1 for _ in range(26)]
        N = M
        for _ in range(N):
            line = input().split()
            if len(line) == 1:
                M = int(line[0])
                break
            node = ord(line[0]) - 65
            links = int(line[1])
            for i in range(1, links + 1):
                cost = int(line[i * 2 + 1])
                nxt = ord(line[i * 2]) - 65
                pq.put((cost, nxt, node))

        print(mst())
