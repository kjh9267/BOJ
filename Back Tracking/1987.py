'''
from array import array

n, m = map(int, input().split())
a = [array('i', map(lambda t: ord(t) - 65, input())) for _ in range(n)]
s = {(0, 0, 67108863)}
r = -1
while s:
    S = list()
    for x, y, z, in s:
        if 0 <= x < n and 0 <= y < m and z >> a[x][y] & 1:
            z ^= 1 << a[x][y]
            S += [
                (x + 1, y, z),
                (x - 1, y, z),
                (x, y + 1, z),
                (x, y - 1, z)
            ]
    s = set(S)
    r += 1
print(r)
'''

'''
R=input;n,m=map(int,R().split());a=[R()for i in[0]*n];r=-1;s=[0]*3,
while s:
 S=[];r+=1
 for x,y,z in s:
  if n>x>=0<=y<m>=1>z>>ord(a[x][y])-65&1:z|=1<<ord(a[x][y])-65;S+=(x+1,y,z),(x-1,y,z),(x,y+1,z),(x,y-1,z)
 s={*S}
print(r)
'''

'''
import collections


def bfs():
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    q = collections.deque()
    q.append((0, 0, board[0][0]))
    max_size = 1

    while q:
        y, x, data = q.popleft() # 0 0 C / 0 1 CA / 1 1 CAD
        for dy, dx in direct:
            ny = y + dy
            nx = x + dx
            if ny < 0 or nx < 0 or ny >= r or nx >= c:
                continue
            if board[ny][nx] in data:
                continue
            if cache[ny][nx] == data + board[ny][nx]:
                continue
            else:
                cache[ny][nx] = data + board[ny][nx]
                q.append((ny, nx, data + board[ny][nx]))
                max_size = max(max_size, len(data)+1)
    print(max_size) # len("CAD")

r, c = map(int, input().split())
cache = [['']*c for _ in range(r)]
board = []
for i in range(r):
    board.append(input())

bfs()
'''

import sys


def asc(graph,x,y):
        return ord(graph[y][x]) - 65


def dfs(x,y,a):
    global cnt
    if cnt < a:
        cnt = a
    if a == max:
        return
    for i,j in zip(dx,dy):
        xx = x + i
        yy = y + j
        if 0 <= xx < c and 0 <= yy < r:
            z = asc(graph, xx, yy)
            if visit[z]:
                continue
            visit[z] = 1
            dfs(xx,yy,a+1)
            visit[z] = 0


r, c = map(int,sys.stdin.readline().split())
graph = [list(sys.stdin.readline().rstrip()) for i in range(r)]
max = len(set([i for row in graph for i in row]))
visit = [0 for _ in range(26)]
visit[asc(graph,0,0)] = 1
dx = (1,0,-1,0)
dy = (0,1,0,-1)
cnt = 0

dfs(0,0,1)

print(cnt)