import sys
from collections import deque


def change(char):
    if ord(char) <= 90:
        return ord(char) - 65
    else:
        return ord(char) - 97 + 26


n = int(sys.stdin.readline())
inf = float('inf')
capacity = [[0 for j in range(52)] for i in range(52)]
flow = [[0 for j in range(52)] for i in range(52)]
total = 0

for _ in range(n):
    u, v, w = sys.stdin.readline().split()
    u = change(u)
    v = change(v)
    w = int(w)
    capacity[u][v] += w
    capacity[v][u] += w

while True:
    queue = deque()
    queue.append(0)
    way = [-1 for _ in range(52)]
    while queue:
        key = False
        x = queue.popleft()
        for i in range(52):
            if capacity[x][i] - flow[x][i] > 0 and way[i] is -1:
                way[x] = i
                queue.append(i)
                if i is 25:
                    key = True
                    break
        if key is True:
            break
    if 25 not in way:
        break
    f = inf
    for i, j in enumerate(way):
        if j is not -1:
            if f > capacity[i][j] - flow[i][j]:
                f = capacity[i][j] - flow[i][j]
    for i, j in enumerate(way):
        if j is not -1:
            flow[i][j] += f
            flow[j][i] -= f
    total += f

print(total)