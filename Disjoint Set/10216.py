# https://www.acmicpc.net/problem/10216


def find(node):
    if parent[node] == node:
        return node
    parent[node] = find(parent[node])
    return parent[node]


def merge(A, B):
    A = find(A)
    B = find(B)
    if A == B:
        return
    if rank[A] < rank[B]:
        A, B = B, A
    parent[B] = A
    if rank[A] == rank[B]:
        rank[A] += 1


def is_adjacent(A, B):
    a_x, a_y, a_r = points[A]
    b_x, b_y, b_r = points[B]
    dist = (a_x - b_x) * (a_x - b_x) + (a_y - b_y) * (a_y - b_y)
    return dist <= (a_r + b_r) * (a_r + b_r)


def solve():
    for A in range(N):
        for B in range(A, N):
            if not is_adjacent(A, B):
                continue
            merge(A, B)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    T = int(input())
    res = list()

    for _ in range(T):
        N = int(input())
        points = [list() for _ in range(N)]
        parent = [point for point in range(N)]
        rank = [0 for _ in range(N)]
        cnt = 0

        for idx in range(N):
            x, y, R = map(int, input().split())
            points[idx] = [x, y, R]

        solve()

        for node, value in enumerate(parent):
            if node == value:
                cnt += 1

        res.append(cnt)

    print('\n'.join(map(str, res)))