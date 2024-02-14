import re
from collections import defaultdict
import math

data = open('in20').read().strip().split('\n')
data = [[int(i) for i in re.findall(r'-?\d+',j)] for j in data]

mina = 1000000
maxa = 0
mini = maxi = 0
for i in range(len(data)):
    x,y,z,vx,vy,vz,ax,ay,az = data[i]
    if abs(ax)+abs(ay)+abs(az) < mina:
        mina = abs(ax)+abs(ay)+abs(az)
        mini = i
    if abs(ax)+abs(ay)+abs(az) > maxa:
        maxa = abs(ax)+abs(ay)+abs(az)
        maxi = i

print(mini)

#Part 2:
def pos(t,p,v,a):
    x,y,z = p
    vx,vy,vz = v
    ax,ay,az = a
    x = x + t*(t+1)/2*ax+t*vx
    y = y + t*(t+1)/2*ay+t*vy
    z = z + t*(t+1)/2*az+t*vz
    return x,y,z

for t in range(40):
    positions = defaultdict(list)
    for i in data:
        for n in range(3):
            i[3+n] += i[6+n]
            i[0+n] += i[3+n]
        # p = pos(t,p,v,a)
        p = (i[0],i[1],i[2])
        positions[p].append((i))

    for i in positions:
        if len(positions[i]) > 1:
            for j in positions[i]:
                data.remove(j)

print(len(data))


def t(x1,x2,vx1,vx2,ax1,ax2): 
    a = 0.5*(ax1-ax2)
    b = (0.5*ax1+vx1)-(0.5*ax2+vx2)
    c = x1-x2
    t = []
    if a == 0:
        if b == 0:
            if x1 == x2:
                return [True]
            return False
        t.append(-c/b)
    else:
        D = b**2-4*a*c
        if D > 0:
            t1 = (-b-math.sqrt(D))/(2*a)
            t2 = (-b+math.sqrt(D))/(2*a)
            if t1 > 0: 
                t.append(t1)
            if t2 > 0: 
                t.append(t2)
    return t

def inter(p1,p2):
    x1,y1,z1,vx1,vy1,vz1,ax1,ay1,az1 = p1
    x2,y2,z2,vx2,vy2,vz2,ax2,ay2,az2 = p2
    tx = t(x1,x2,vx1,vx2,ax1,ax2)
    ty = t(y1,y2,vy1,vy2,ay1,ay2)
    tz = t(z1,z2,vz1,vz2,az1,az2)
    if tx == False or ty == False or tz == False:
        return False
    ts = [tx,ty,tz]
    for a in tx:
        for b in ty:
            for c in tz:
                l = [a,b,c]
                while True in l:
                    l.remove(True)
                if len(set(l))==1:
                    return(int(list(set(l))[0]))
                    print('True')
                    
                if a == b == c:
                    return int(a)
    return False
    
timematrix = []
for i in range(len(data)):
    for j in range(i,len(data)):
        if i != j:
            tij = inter(data[i],data[j])
            if tij != False:
                timematrix.append((tij,i,j))


print('check:',sorted(timematrix))

removed = []
ot = 0
l = []
for ts,a,b in sorted(timematrix):
    if ts == ot:
        l.append(a)
        l.append(b)
        if a not in removed:
            removed.append(a)
        if b not in removed:
            removed.append(b)
    else:
        ot = ts
        for i in l:
            for j in timematrix[::-1]:
                if i in j:
                    timematrix.remove(j)
        l = []
  
print(removed)    
print(len(data)-len(set(removed)))

#too low 546
#too high 574