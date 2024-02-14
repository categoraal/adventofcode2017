from collections import defaultdict
data = open('in23').read().strip().split('\n')
regs = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}

def coprocessor(regs,part):
    p = 0
    cnt = 0
    tel = 0
    while p < len(data):
        tel += 1
        ins,X,Y = data[p].split()
        v1 = regs[X] if X in regs else int(X)
        v2 = regs[Y] if Y in regs else int(Y)
        if p == 11 and part:
            p = 20
            if regs['b']/regs['d'] != 1 and regs['b']%regs['d']==0:
                regs['f'] = 0
            regs['e'] = regs['b']
            regs['g'] = 0  
            continue
        if ins == 'set':
            regs[X] = v2
            p += 1
        if ins == 'sub':
            regs[X] -= v2
            p += 1
        if ins == 'mul':
            cnt += 1
            regs[X] *= v2
            p += 1
        if ins == 'jnz':
            p += v2 if v1 != 0 else 1
    print('p1:',cnt)
    print(regs)
    return 0

regs = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
coprocessor(regs,False)
regs = {'a':1,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0}
coprocessor(regs,True)