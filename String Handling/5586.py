s = raw_input()
cnt = 0
print s.count('JOI')
for i in range(1,len(s)-1):
    if s[i] == 'O':
        if s[i-1] == 'I' and s[i+1] == 'I':
            cnt += 1
print cnt