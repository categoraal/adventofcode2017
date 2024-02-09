data = open('in9').read().strip()

gar = False
d = idx = p1 = p2 = 0
while idx < len(data):
    c = data[idx]
    if c == '<' and gar == False:
        gar = True
        p2 -= 1
    if c == '>' and gar:
        gar = False
    if c == '{' and gar == False:
        d += 1
        p1 += d
    if c == '}' and gar == False:
        d -= 1
    if c == '!' and gar:
        idx += 2
    else:
        if gar and data[idx] != '!':
            p2 += 1
        idx += 1

print(p1)
print(p2)