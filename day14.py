from itertools import accumulate
from operator import xor
from collections import defaultdict
data = open('in14').read().strip()

def knot(data,l,idx=0,skip=0):
    for _ in range(64):
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
            idx = (idx+i+skip)%len(l)
            skip+=1    
    return l

def densehash(l):
    p2 = res =  ''
    for i in range(16):
        p2 += str(hex(list(accumulate(l[16*i:16*i+16],xor))[-1])[2:]).zfill(2)
    for i in p2:
        res += bin(int(i,16))[2:].zfill(4)
    return res

res = 0
k = []
for i in range(128):
    d = [ord(i) for i in str(data)+'-'+str(i)]+[17,31,73,47,23]
    l= knot(d,[i for i in range(256)],0,0)
    k.append(densehash(l))
    res += densehash(l).count('1')
print(res)

def dfs(x):
    queue = [x];dirs = ((1,0),(0,1),(-1,0),(0,-1))
    seen.add(x)
    for r,c in queue:
        for dr,dc in dirs:
            nr = r+dr;nc = c+dc
            if 0 <= nr < len(k) and 0 <= nc < len(k[0]) and  (nr,nc) not in seen:
                if k[nr][nc] == '1':
                    queue.append((nr,nc))
                    seen.add((nr,nc))

seen = set()
cnt = 0
for r in range(len(k)):
    for c in range(len(k[0])):
        if k[r][c] == '1' and (r,c) not in seen:
            cnt += 1
            dfs((r,c))

print(cnt)