import sys
from queue import PriorityQueue

n, m = map(int,sys.stdin.readline().split())
cards = list(map(int,sys.stdin.readline().split()))
pq = PriorityQueue()

for i in cards:
    pq.put(i)

for _ in range(m):
    first = pq.get()
    second = pq.get()
    new = first + second
    pq.put(new)
    pq.put(new)

print(sum(pq.queue))