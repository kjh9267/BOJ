import sys
n = int(sys.stdin.readline())
a = n
cnt = 0
while True:
    if a < 10:
        a = a*10 + a
    else:
        b = a/10 + a%10
        a = (a%10)*10 + b%10
    cnt += 1
    if a == n:
        print cnt
        exit()