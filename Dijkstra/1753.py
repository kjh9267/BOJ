import sys
from queue import PriorityQueue

v, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
inf = float('inf')
graph = [[] for _ in range(v)]
# 간선의 도착점을 입력하기 위한 list (노드수가 20000이기 때문에 v*v 행렬은 약 1.6GB로 메모리 초과)
# 출발점과 도착점이 같고 비용이 다른 경우를 위해서도 v*v를 사용하지 않는다.
cost = [[] for _ in range(v)]           # 간선의 비용을 입력하기 위한 list

for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)      # 간선의 도착점
    cost[a-1].append(c)         # 간선의 비용

pq = PriorityQueue()      # 우선순위 큐
pq.put((0,k-1))         # 우선순위 큐에 시작점만 거리를 0으로 하여 넣어준다
res = [inf for _ in range(v)]   # 결과 값을 저장하기 위한 list
res[k-1] = 0            # 출발 점의 결과 값은 0으로 초기화

while pq.qsize():                 # 우선순위 큐가 빌 때까지 반복
    dist, node = pq.get()         # 최소거리와 그 노드를 우선순위큐에서 get
    if res[node] < dist:        # 이미 나온 결과 값 보다 더 큰 비용이 들어온 경우 우선순위 큐에서 다시 get
        continue
    for i, j in zip(graph[node], cost[node]):   # 간선의 도착점과 그에 대한 비용
        if res[i] > j + dist:      # 도착점의 비용과 도착점의 비용 + 전 노드까지의 값을 비교
            res[i] = j + dist      # 도착점의 비용이 더 클 경우 도착점의 비용 + 전 노드까지의 값으로 변경
            pq.put((res[i], i))         # 갱신된 값을 우선순위 큐에도 넣어준다

for i in res:
    if i is not inf:
        print(i)
    else:
        print('INF')