import sys
from queue import PriorityQueue


def asc(char):
    if 65 <= ord(char) < 91:
        return ord(char) - 65
    elif 97 <= ord(char) < 123:
        return ord(char) - 71


n, m, t, d = map(int,sys.stdin.readline().split())
graph = [list(map(asc,list(sys.stdin.readline().rstrip()))) for _ in range(n)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
inf = float('inf')
pq = PriorityQueue()
pq.put((0, (0, 0)))
res = [[inf for __ in range(m)] for _ in range(n)]
res[0][0] = 0
while pq.qsize():
    dist, node = pq.get()
    if dist > res[node[1]][node[0]]:
        continue
    for i, j in zip(dx, dy):
        x = node[0] + i
        y = node[1] + j
        if 0 <= x < m and 0 <= y < n:
            length = graph[y][x] - graph[node[1]][node[0]]
            if -t <= length <= 0:
                if res[y][x] > dist + 1:
                    res[y][x] = dist + 1
                    pq.put((res[y][x], (x, y)))
            elif 0 < length <= t:
                if res[y][x] > dist + (length ** 2):
                    res[y][x] = dist + (length ** 2)
                    pq.put((res[y][x], (x, y)))

pq = PriorityQueue()
pq.put((0, (0, 0)))
res2 = [[inf for __ in range(m)] for _ in range(n)]
res2[0][0] = 0
while pq.qsize():
    dist, node = pq.get()
    if dist > res2[node[1]][node[0]]:
        continue
    for i, j in zip(dx, dy):
        x = node[0] + i
        y = node[1] + j
        if 0 <= x < m and 0 <= y < n:
            length = graph[node[1]][node[0]] - graph[y][x]
            if -t <= length <= 0:
                if res2[y][x] > dist + 1:
                    res2[y][x] = dist + 1
                    pq.put((res2[y][x], (x, y)))
            elif 0 < length <= t:
                if res2[y][x] > dist + (length ** 2):
                    res2[y][x] = dist + (length ** 2)
                    pq.put((res2[y][x], (x, y)))

result = []

for i in range(n):
    for j in range(m):
        if res[i][j] + res2[i][j] <= d:
            result.append(graph[i][j])

print(max(result))