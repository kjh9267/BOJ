import sys

string = []

while True:
    s = sys.stdin.readline().rstrip()
    if not s:
        break
    string.append(s)

string = ''.join(string)
res = []
res2 = []

for i in map(chr,range(97,123)):
    res.append(string.count(i))

if res.count(max(res)) > 1:
    for j in range(26):
        if max(res) == res[j]:
            res2.append(chr(j + 97))
else:
    for i in res:
        print(chr(res.index(max(res)) + 97))
        exit()

print(''.join(res2))