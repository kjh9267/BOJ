a = raw_input()
b= []
for i in range(len(a)):
    if ord(a[i]) == 65:
        b.append('X')
    elif ord(a[i]) == 66:
        b.append('Y')
    elif ord(a[i]) == 67:
        b.append('Z')
    else:
        b.append(chr(ord(a[i]) - 3))
print "".join(b)