from collections import defaultdict
data = [i.split(' <-> ') for i in open('in12').read().strip().split('\n')]

graph = defaultdict(list)
notseen = set()
for a,b in data:
    notseen.add(a)
    b = b.split(', ')
    graph[a] += b
    if type(b) != list:
        print(b,type(b))
    for i in b:
        graph[i] += [a]

def findgroup(start):
    queue = [start]
    seen = set()
    for i in queue:
        seen.add(i)
        for v in graph[i]:
            if v not in queue and v not in seen:
                queue.append(v)
    return seen

seen = findgroup('0')
print(len(seen))

p2 = 0
while len(notseen) > 0:
    start = list(notseen)[0]
    seen = findgroup(start)
    notseen = notseen - seen
    p2 += 1

print(p2)