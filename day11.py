data = open('in11').read().strip().split(',')
ne = nw = n = s = sw = se = 0
p = []
for i in data:
    if i == 'ne':
        ne += 1
    if i == 'se':
        se += 1
    if i == 'n':
        n+= 1
    if i == 's':
        s += 1
    if i == 'sw':
        sw += 1
    if i == 'nw':
        nw += 1
    p.append(max([(ne-sw),(nw-se)])+(n-s))

print(p[-1])
print(max(p))