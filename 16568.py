import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(N)
    cnt = 0
    while queue:
        length = len(queue)
        temp = list()
        cnt += 1
        for _ in range(length):
            cur = queue.popleft()
            if visited[0]:
                return visited[0]
            nxt = cur - 1
            if nxt >= 0 and not visited[nxt]:
                queue.append(nxt)
                temp.append(nxt)
            nxt = cur - a
            if nxt >= 0 and not visited[nxt]:
                if nxt == 0:
                    temp.append(nxt)
                else:
                    queue.append(nxt - 1)
                    temp.append(nxt - 1)
            nxt = cur - b
            if nxt >= 0 and not visited[nxt]:
                if nxt == 0:
                    temp.append(nxt)
                else:
                    queue.append(nxt - 1)
                    temp.append(nxt - 1)
        for i in temp:
            visited[i] = cnt


N, a, b = map(int,sys.stdin.readline().split())
visited = [0 for _ in range(N + 1)]
bfs()

if N == 0:
    print(0)
else:
    print(visited[0])