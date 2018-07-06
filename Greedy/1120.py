import sys


a, b = sys.stdin.readline().split()
length = len(a)
diff = len(b) - len(a) + 1
result = float('inf')


for i in range(diff):
    cnt = 0
    for j in range(length):
        if a[j] != b[j + i]:
            cnt += 1
    result = min(result,cnt)

print(result) 