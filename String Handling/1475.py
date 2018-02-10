a = raw_input().replace('9','6')
b = list(set(a))
cnt = []
for i in range(len(b)):
    if b[i] == '6':
        cnt.append((a.count(b[i])+1)/2)
    else:
        cnt.append(a.count(b[i]))
print max(cnt)