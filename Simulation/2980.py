import sys

n, l = map(int,sys.stdin.readline().split())
graph = [0 for _ in range(l)]
car = 0
time = 0

for _ in range(n):
    d, r, g = map(int,sys.stdin.readline().split())
    graph[d-1] = (r, g)

while car != l-1:
    if graph[car] is 0:
        time += 1
        car += 1
    else:
        r, g = graph[car]
        x = time % (r + g)
        if x < r:
            time += 1
        else:
            time += 1
            car += 1
print(time)