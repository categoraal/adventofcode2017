data = int(open('in17').read().strip())

def solve(n):
	buffer = [0]
	idx = 0
	for i in range(1,n+1):
		idx = (idx+data)%len(buffer)+1
		buffer.insert(idx,i)
	return buffer

buffer = solve(2017)
print(buffer[buffer.index(2017)+1])

def solve2(n):
	l = 1
	idx = 0
	i = 1
	while i < n:
		idx = (idx+data)%l+1
		if idx == 1:
			res = i
		l+=1
		i+=1	
	return res

print(solve2(5*10**7))
