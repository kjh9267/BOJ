import sys
from collections import deque
# 파이썬에서 일반 list를 사용하여 큐를 구현하면 pop의 시간 복잡도가 O(n)이 되서 collections의 deque를 사용


def dfs():
    stack = deque()
    stack.append(v)
    visit = []
    while stack:                # 스택이 빌 때 까지 반복
        x = stack.pop()         # 가장 마지막에 들어온 요소 pop
        if x not in visit:      # visit에 x가 없다면 visit에 append
            visit.append(x)
            for i in range(n-1,-1,-1):          # 인접한 작은 수 부터 탐색하는 조건을 만족 시키기 위해 반대로
                if graph[x-1][i] is 1:  # 1 인경우(인접노드)
                    stack.append(i+1)
    return visit


def bfs():
    queue = deque()
    queue.append(v)
    visit = []
    while queue:
        x = queue.popleft()     # deque의 popleft를 사용 하여 pop
        visit.append(x)
        for i in range(n):
            if graph[x-1][i] is 1:      # 인접한 노드들 중에서
                if i+1 not in visit and i+1 not in queue:   # 아직 visit하지 않고, queue에 있지 않은 노드만 append
                    queue.append(i+1)
    return visit


n, m, v = map(int,sys.stdin.readline().split())
graph = [[0 for j in range(n)] for i in range(n)]       # 인접 행렬
for _ in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a-1][b-1] = 1         # 인접 노드를 1로 표현
    graph[b-1][a-1] = 1
print(" ".join(map(str,dfs())))
print(" ".join(map(str,bfs())))