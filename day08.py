from collections import defaultdict
data = [i.split() for i in open('in8').read().strip().split('\n')]

regs = defaultdict(int)
print(regs['a'])

p2 = 0
for ins in data:
    if eval(str(regs[ins[-3]])+ins[-2]+ins[-1]):
        if ins[1] == 'inc':
            regs[ins[0]] += int(ins[2])
        else:
            regs[ins[0]] -= int(ins[2])
        if regs[ins[0]] > p2:
            p2 = regs[ins[0]]

mx = 0
for i in regs:
    if regs[i] > mx:
        mx = regs[i]

print(mx)
print(p2)