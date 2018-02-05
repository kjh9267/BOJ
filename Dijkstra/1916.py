import sys
from queue import PriorityQueue  # 최단 거리를 구하기 위해 우선순위큐 사용

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
inf = float('inf')
graph = [[] for _ in range(n)]  # 출발점과 도착점이 같고 비용이 다른 경우를 위해 n*n 행렬 사용 하지 않음
cost = [[] for _ in range(n)]  # 간선의 비용을 입력하기 위한 list

for _ in range(m):
    a, b, c = map(int,sys.stdin.readline().split())
    graph[a-1].append(b-1)  # 간선의 도착점
    cost[a-1].append(c)     # 간선의 비용
x, y = map(int,sys.stdin.readline().split())

res = [inf for j in range(n)]
res[x-1] = 0

pq = PriorityQueue()  # 우선순위 큐 사용
pq.put((0,x-1))       # 출발점의 값만 0으로 넣어준다

while pq.qsize():               # 우선순위 큐가 빌 때 까지 반복
    dist, node = pq.get()       # 현재노드 까지의 최소값과 현재 노드
    if res[node] < dist:
        continue
    for i, j in zip(graph[node], cost[node]):   # 간선의 도착점과 그에 대한 비용
        if res[i] > j + dist:      # 도착점의 비용과 현재 노드 까지의 비용 + 도착점 까지의 비용을 비교
            res[i] = j + dist      # 도착점의 비용이 더 클 경우 현재 노드 까지의 비용 + 도착점 까지의 비용으로 변경
            pq.put((res[i], i))         # 갱신된 값을 우선순위 큐에도 넣어준다

print(res[y-1])