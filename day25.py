from collections import defaultdict
data = open('in25').read().strip().split('\n\n')
n = int(data[0].split('\n')[-1].split()[-2])

states = {}
tape = defaultdict(int)
for i in data[1:]:
    i = i.split('\n')
    key = i[0].split()[-1][:-1]
    r = []
    for v in i[1:]:
        v = v.split()[-1][:-1]
        if v == 'left':
            v = -1
        if v == 'right':
            v = 1
        try:
            v = int(v)
        except:
            True
        r.append(v)
    states[key] = r

state = 'A'
p = 0
for _ in range(n):
    val = tape[p]
    c1,w1,m1,s1,c2,w2,m2,s2 = states[state]
    if val == c1:
        tape[p] = w1
        p += m1
        state = s1
    elif val == c2:
        tape[p] = w2
        p += m2
        state = s2

res = 0
for i in tape:
    if tape[i] == 1:
        res += 1
print(res)