import sys
from collections import deque


def bfs(s,cnt=0):
    queue = deque()
    queue.append(s-1)
    level = deque()
    visit = ['x' for _ in range(f)]
    visit[s-1] = 'o'
    while queue:
        x = queue.popleft()
        up = x + u
        down = x - d
        if up < f and visit[up] == 'x':
            level.append(up)
            visit[up] = 'o'
            if graph[up] == 'e':
                return cnt + 1
        if 0 <= down and visit[down] == 'x':
            level.append(down)
            visit[down] = 'o'
            if graph[down] == 'e':
                return cnt + 1
        if not queue:
            queue.extend(level)
            level.clear()
            cnt += 1


f, s, g, u, d = map(int,sys.stdin.readline().split())
graph = ['o' for _ in range(f)]
graph[s-1] = 's'
graph[g-1] = 'e'

if s == g:
    print(0)
    exit()

res = bfs(s)

if res is None:
    print('use the stairs')
else:
    print(res)