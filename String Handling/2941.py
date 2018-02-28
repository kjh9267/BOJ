import sys

s = sys.stdin.readline().rstrip()
cnt = 0
long = 0

for i, j in enumerate(s):
    if j == '-':
        if s[i-1] == 'c' or s[i-1] == 'd':
            cnt += 1
            long += 2
    if j == 'j' and i is not 0:
        if s[i-1] == 'l' or s[i-1] == 'n':
            cnt += 1
            long += 2
    if j == '=' and i is not 1:
        if s[i-2] == 'd' and s[i-1] == 'z':
            cnt += 1
            long += 3
    if j == '=':
        if s[i-1] == 'z':
            try:
                if s[i-2] != 'd':
                    cnt += 1
                    long += 2
            except:
                pass
    if j == '=':
        if s[i-1] == 's' or s[i-1] == 'c':
            cnt += 1
            long += 2

print(cnt + len(s) - long)