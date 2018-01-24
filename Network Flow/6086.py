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
    key = False
    while queue:
        x = queue.popleft()
        for i in range(52):
            if capacity[x][i] - flow[x][i] > 0 and way[i] is -1:
                queue.append(i)
                way[i] = x
                if i is 25:
                    key = True
                    break
        if key is True:
            break
    if way[25] is -1:
        break
    f = inf
    node = 25
    while node is not 0:
        if f > capacity[way[node]][node] - flow[way[node]][node]:
            f = capacity[way[node]][node] - flow[way[node]][node]
        node = way[node]
    node = 25
    while node is not 0:
        flow[way[node]][node] += f
        flow[node][way[node]] -= f
        node = way[node]
    total += f
print(total)