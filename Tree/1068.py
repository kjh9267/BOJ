import sys
from collections import deque

n = int(sys.stdin.readline())
nodes = list(map(int,sys.stdin.readline().split()))
failure = int(sys.stdin.readline())
graph = [[] for _ in range(n)]
root = 0

for index, parent in enumerate(nodes):
    if parent is not -1:
        graph[parent].append(index)
    else:
        root += index

if root is failure:
    print(0)
    exit()

for index, child in enumerate(graph):
    if failure in child:
        graph[index].remove(failure)

queue = deque()
queue.append(root)
res = 0
while queue:
    current = queue.popleft()
    for i in graph[current]:
        if not graph[i]:
            res += 1
        else:
            queue.append(i)

if res is 0:
    print(1)
else:
    print(res)