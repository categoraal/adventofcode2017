from operator import xor
from itertools import accumulate
d = open('in10').read().strip()
data1 = [int(i) for i in d.split(',')]
data2 = [ord(i) for i in d]+[17,31,73,47,23]

def p1(data,l,idx=0,skip=0):
    for i in data:
        end = idx+i
        sl = []
        if end < len(l) or end%len(l) == 0 and i < len(l):
            l[idx:idx+i] = l[idx:idx+i][::-1]
        else:
            end = end%len(l)
            sl = (l[idx:]+l[:end])[::-1] 
            l[:end] = sl[-end:]
            l[idx:] = sl[:-end]
        idx += (i+skip)
        idx = idx%len(l)
        skip+=1
        
    return l[0]*l[1],l,idx,skip

print(p1(data1,[i for i in range(256)])[0])

idx=skip=0
l = [i for i in range(256)]
for i in range(64):
    r,l,idx,skip = p1(data2,l,idx,skip)

p2 = ''
for i in range(16):
    c = str(hex(list(accumulate(l[16*i:16*i+16],xor))[-1])[2:])
    if len(c) == 1:
        c = '0'+c
    p2 += c
print(p2)