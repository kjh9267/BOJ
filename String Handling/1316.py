cnt = 0
for i in range(input()):
    a = raw_input()
    b = list(set(a))
    for u in range(len(b)):
        if len(a) - a[::-1].index(b[u]) - a.index(b[u]) != a.count(b[u]):
            break
    else:
        cnt += 1
print cnt