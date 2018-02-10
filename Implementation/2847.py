a = [input() for i in range(input())]
b = len(a)
cnt = 0
for i in range(b-1,0,-1):
    if a[i] <= a[i-1]:
        while a[i] <= a[i-1]:
            a[i-1] -= 1
            cnt += 1
print cnt