import sys
from collections import deque


def bfs():
    queue = deque()
    queue.append(n)
    level = deque()
    cnt = 0
    while queue:
        z = queue.popleft()
        for i in adds:
            x = z + i
            if 0 <= x < 100001 and visit[x] is 0:
                level.append(x)
                visit[x] = 1
                if x == m:
                    return cnt + 1
        for i in multiples:
            x = z * i
            if 0 <= x < 100001 and visit[x] is 0:
                level.append(x)
                visit[x] = 1
                if x == m:
                    return cnt + 1
        if not queue:
            queue.extend(level)
            level.clear()
            cnt += 1


a, b, n, m = map(int,sys.stdin.readline().split())
graph = [0 for _ in range(100001)]
graph[m] = 1
visit = [0 for _ in range(100001)]
visit[n] = 1
adds = (-1,1,-a,a,-b,b)
multiples = (a,b)

print(bfs())