input = __import__('sys').stdin.readline

N, M = map(int,input().split())
data = list(map(int,input().split()))
add = sum(data[:M])
res = add
for i in range(M,N):
    # print(i, i-M, data[i], data[i-M])
    add -= data[i-M]
    add += data[i]
    if res < add:
        res = add

print(res)