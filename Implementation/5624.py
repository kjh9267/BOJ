n = input()
a = map(int,raw_input().split())
cnt = 0
for i in range(3,len(a)):
    if a[i] == a[i-1] + a[i-2] + a[i-3]:
        cnt += 1
print cnt