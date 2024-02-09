from collections import defaultdict
from copy import deepcopy
data = [i.split() for i in open('in7').read().strip().split('\n')]

set1 = set()
set2 = set()
weigths = {}
graph = defaultdict(list)
for i in data:
    set1.add(i[0])
    weigths[i[0]] = int(i[1][1:-1])
    graph[i[0]] = []
    if len(i) > 2:
        for k in i[3:]:
            if k[-1] == ',':
                set2.add(k[:-1])
                graph[i[0]].append(k[:-1])
            else:
                set2.add(k)
                graph[i[0]].append(k)
p1 = set1-set2
for i in p1:
    p1 = i
    print(i)

weigths2 = deepcopy(weigths)

def f(x,con):
    w = weigths[x]
    ws = []
    if graph[x] != []:
        for i in graph[x]:
            a,con = f(i,con)
            ws.append(a)
    if len(set(ws)) != 1 and set(ws) != set() and con:
        w1=w2=0
        for i in ws:
            if ws.count(i) == 1:
                w1 = i
            if ws.count(i) != 1:
                w2 = i
        d = w1-w2
        for k in weigths:
            if weigths[k] == w1 and k in graph[x]:
                print(weigths2[k]-d)
        con = False
    w += sum(ws)
    weigths[x] = w
    return w,con

f(p1,True)