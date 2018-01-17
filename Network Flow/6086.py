import sys
from collections import deque


def change(char):
    if ord(char) <= 90:
        return ord(char) - 65
    else:
        return ord(char) - 97 + 26


def bfs():
    queue = deque()
    queue.append(0)
    way = [0]
    key = False
    while queue:
        x = queue.popleft()
        visit.append(x)
        for i in range(52):
            if capacity[x][i] - flow[x][i] > 0:
                if i not in visit and i not in queue:
                    queue.append(i)
                    way.append(i)
                    if i is 25:
                        key = True
                        break
        if key is True:
            break
    return way


n = int(sys.stdin.readline())
inf = float('inf')
capacity = [[0 for j in range(52)] for i in range(52)]
flow = [[0 for j in range(52)] for i in range(52)]
visit = []
total = 0

for _ in range(n):
    u, v, w = sys.stdin.readline().split()
    u = change(u)
    v = change(v)
    w = int(w)
    capacity[u][v] += w

while True:
    res = bfs()
    print(res)
    if res[-1] is not 25:
        break
    f = inf
    for i in range(len(res)-1):
        if f > capacity[res[i]][res[i+1]] - flow[res[i]][res[i+1]]:
            f = capacity[res[i]][res[i+1]] - flow[res[i]][res[i+1]]
    for i in range(len(res)-1):
        flow[res[i]][res[i+1]] += f
        flow[res[i]][res[i+1]] -= f
    total += f
    print(total)