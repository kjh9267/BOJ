import sys
from collections import deque


def bfs(x):
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        for i in (a-1,a+1,a*2):
            if 0 <= i < 100001 and way[i] == 'x':
                queue.append(i)
                way[i] = a
                if i == k:
                    return


n, k = map(int,sys.stdin.readline().split())
graph = ['x' for _ in range(100001)]
way = ['x' for _ in range(100001)]
way[n] = 'o'
cnt = 0

bfs(n)

while k != n:
    cnt += 1
    k = way[k]

print(cnt)