# https://www.acmicpc.net/problem/1993

import sys
sys.setrecursionlimit(999999999)


def dfs(name, cur, acc, score):
    if cur == N + 1:
        res[name] = max(res[name], score)
        return
    for nxt, dist, s in adj[cur]:
        if people[name] < acc + dist:
            continue
        dfs(name, nxt, acc + dist, score + s)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    T = 0
    while True:
        T += 1
        N = int(input())
        if N == 0:
            break
        data = [[0, 0, 0]] + [list(map(int,input().split())) for idx in range(N)]
        adj = [list() for _ in range(N + 1)]

        for cur in range(N + 1):
            for nxt, value in enumerate(data):
                if cur >= nxt:
                    continue
                nx, ny, s = value
                x, y, _ = data[cur]
                adj[cur].append((nxt, ((nx - x) ** 2 + (ny - y) ** 2) ** (1 / 2), s))
            if cur == 0:
                continue
            adj[cur].append((N + 1, (data[cur][0] ** 2 + data[cur][1] ** 2) ** (1 / 2), 0))
        res = dict()
        people = dict()
        order = list()
        while True:
            name, health = input().split()
            health = int(health)
            if name == '#' and health == 0:
                break
            people[name] = health
            order.append((name, health))
            res[name] = 0
        for name in people.keys():
            dfs(name, 0, 0, 0)
        print('Race {}'.format(T))
        for name, health in order:
            print('{}: {}'.format(name, res[name]))