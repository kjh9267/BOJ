a = [raw_input() for i in range(8)]
cnt = 0
for i in range(0,8,2):
    for u in range(0,8,2):
        if a[i][u] == 'F':
            cnt += 1
for i in range(1,8,2):
    for u in range(1,8,2):
        if a[i][u] == 'F':
            cnt += 1
print cnt