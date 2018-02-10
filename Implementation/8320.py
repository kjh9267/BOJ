n = input()
cnt = 0
for i in range(n):
    if n%(i+1) == 0:
        cnt += n/(i+1)
print cnt