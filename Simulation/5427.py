import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    w, h = map(int,sys.stdin.readline().split())
    graph = [['$' for j in range(w+2)] for i in range(h+2)]
    