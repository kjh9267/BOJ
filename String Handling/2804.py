import sys

a, b = sys.stdin.readline().strip().split()
graph = [['.' for j in range(len(a))] for i in range(len(b))]

for i, char in enumerate(a):
    if char in b:
        same = i
        start = b.index(char)
        break

graph[start] = list(a)

for i, stirngs in enumerate(graph):
    stirngs[same] = b[i]

print("\n".join(map("".join,graph)))