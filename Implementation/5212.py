import sys

r, c = map(int,sys.stdin.readline().split())
graph = [['.' for j in range(c+2)] for i in range(r+2)]
melt = [[0 for j in range(c+2)] for i in range(r+2)]
dx = (1,0,-1,0)
dy = (0,1,0,-1)
x1,x2,y1,y2 = 1, 1, 1, 1

for i in range(r):
    x = list(sys.stdin.readline().rstrip())
    for j, u in enumerate(x):
        graph[i+1][j+1] = u

for i in range(1,r+1):
    for j in range(1,c+1):
        if graph[i][j] == 'X':
            for xx, yy in zip(dx,dy):
                if graph[i + yy][j + xx] == '.':
                    melt[i][j] += 1

for i in range(1,r+1):
    for j in range(1,c+1):
        if melt[i][j] > 2:
            graph[i][j] = '.'

for i in range(1,r+1):
    if 'X' in graph[i]:
        y1 = i
        break

for i in range(r+1,0,-1):
    if 'X' in graph[i]:
        y2 = i
        break

key = False
for i in range(1,c+1):
    for j in range(1,r+1):
        if graph[j][i] == 'X':
            x1 = i
            key = True
            break
    if key is True:
        break

key = False
for i in range(c+1,0,-1):
    for j in range(1,r+1):
        if graph[j][i] == 'X':
            x2 = i
            key = True
            break
    if key is True:
        break

res = [[] for i in range(y2-y1+1)]

for u, i in enumerate(list(range(y1,y2+1))):
    for j in range(x1,x2+1):
        res[u].append(graph[i][j])

for i in res:
    print(''.join(i))