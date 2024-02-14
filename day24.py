from functools import cache
data = open('in24').read().strip().split('\n')

graph = {}
for i in data:
    a,b = [int(j) for j in i.split('/')]
    if a in graph:
        graph[a].append(b)
    else:
        graph[a] = [b]

    if b in graph:
        graph[b].append(a)
    else:
        graph[b] = [a]

@cache
def path(x=0,currentpath=(0,0)):
    res = [0]
    dests = graph[x]
    for i in dests:
        if (x,i) not in currentpath:
            cpath = list(currentpath)
            cpath += [(x,i),(i,x)]
            res.append(x+path(i,tuple(cpath)))
    return x+max(res)

@cache
def longpath(x=0,currentpath=(0,0),l=0):
    res = [(0,0)]
    dests = graph[x]
    for i in dests:
        if (x,i) not in currentpath:
            cpath = list(currentpath)
            cpath += [(x,i),(i,x)]
            ll,dd = longpath(i,tuple(cpath),l+1)
            res.append((ll+1,x+dd))
    l,d = max(sorted(res,reverse=True))
    d += x
    return l,d

print(path())
print(longpath()[1])