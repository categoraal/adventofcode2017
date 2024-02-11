from collections import defaultdict,deque

data = [i.split() for i in open('in18').read().strip().split('\n')]

regs = {};regs0 = {};regs1 ={}
for i in data:
	if  i[1].isnumeric() == False:
		regs[i[1]] = 0
		regs0[i[1]] = 0
		regs1[i[1]] = 0


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

def program(data,p,received,state):
	sig = deque()
	cnt = 0
	regs = state
	while 0 <= p < len(data):
		ins = data[p]
		c = ins[0]
		v1 = regs[ins[1]] if (ins[1] in regs) else int(ins[1])
		if len(ins) == 3:
				v2 = regs[ins[2]] if ins[2] in regs else int(ins[2])
		if c == 'snd':
			sig.append(v1)
			cnt += 1
		if c == 'set':
			regs[ins[1]] = v2
		if c == 'add':
			regs[ins[1]] += v2
		if c == 'mul':
			regs[ins[1]] =	v1*v2
		if c == 'mod':
			regs[ins[1]] = v1%v2
		if c == 'rcv':
			if len(received) == 0:
				break
			else:
				regs[ins[1]] = received.popleft()
		if c == 'jgz':
			if v1 > 0:
				p += v2-1
		p+=1
	return p,sig,regs,cnt

pointer0 = pointer1 = 0
s1 = s0 = []
score = 0
regs1['p'] = 1
condition = True
while condition:
	pointer0,s0,regs0,_ = program(data,pointer0,s1,regs0)
	pointer1,s1,regs1,cnt = program(data,pointer1,s0,regs1)
	score += cnt
	if len(s0) == len(s1) == 0:
		condition = False
		break

print(score)