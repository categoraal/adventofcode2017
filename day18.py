from collections import defaultdict
data = [i.split() for i in open('in18').read().strip().split('\n')]

regs = {}
for i in data:
	if  i[1].isnumeric() == False:
		regs[i[1]] = 0


def p1(data):
	p = 0
	sounds = []
	while 0 <= p < len(data):
		ins = data[p]
		c = ins[0]
		v1 = regs[ins[1]] if (ins[1] in regs) else int(ins[1])
		if len(ins) == 3:
				v2 = regs[ins[2]] if ins[2] in regs else int(ins[2])
		if c == 'snd':
			sounds.append(v1)
		if c == 'set':
			regs[ins[1]] = v2
		if c == 'add':
			regs[ins[1]] += v2
		if c == 'mul':
			regs[ins[1]] =	v1*v2
		if c == 'mod':
			regs[ins[1]] = v1%v2
		if c == 'rcv':
			if v1 != 0:
				rcv = sounds[-1]
				break
		if c == 'jgz':
			if v1 > 0:
				p += v2-1
		p+=1
	return rcv

print(p1(data))
