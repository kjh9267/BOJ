n, m = map(int,raw_input().split())
l = map(int,raw_input().split())
x = []
for i in range(n):
    for u in range(n):
        for y in range(n):
            if (i == u) | (i == y) | (y == u):
                pass
            else:
                if l[i] + l[u] + l[y] <= m:
                    x.append(l[i] + l[u] + l[y])
print max(x)