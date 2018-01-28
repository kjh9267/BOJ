from sys import stdin


def match(a):
    visit[a] = 1
    for b in graph[a]:
        if B[b] is -1:
            A[a] = b
            B[b] = a
            return True
        elif visit[B[b]] is 0 and match(B[b]):
            A[a] = b
            B[b] = a
            return True
    return False


n, m = map(int,stdin.readline().split())
graph = [[] for _ in range(n)]
A = [-1 for _ in range(n)]
B = [-1 for _ in range(m)]
cnt = 0

for i in range(n):
    x = list(map(int,stdin.readline().split()))[1:]
    for j in x:
        graph[i].append(j-1)

for i in range(n):
    if A[i] is -1:
        visit = [0 for _ in range(n)]
        if match(i):
            cnt += 1
print(cnt)