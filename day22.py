from collections import defaultdict
data = open('in22t').read().strip().split('\n')

kaart = defaultdict(str)
for r in range(len(data)):
    for c in range(len(data[0])):
        kaart[(r,c)] = data[r][c]

pos = (int((len(data)-1)/2),int((len(data[0])-1)/2))

d = (-1,0)
left = {(0,-1):(1,0),(-1,0):(0,-1),(0,1):(-1,0),(1,0):(0,1)}
right = {(1,0):(0,-1),(0,-1):(-1,0),(-1,0):(0,1),(0,1):(1,0)}
cnt = 0
for _ in range(10000):
    c = kaart[pos]
    d = right[d] if c == '#' else left[d]
    cnt += 1 if c != '#' else 0
    kaart[pos] = '.' if c == '#' else '#'
    r,c = pos; dr,dc = d
    pos = (r+dr,c+dc)

print(cnt)

#part 2
def f(c): return lambda: c
kaart = defaultdict(f('.'))
for r in range(len(data)):
    for c in range(len(data[0])):
        kaart[(r,c)] = data[r][c]

d = (-1,0)      
cnt = 0
pos = (int((len(data)-1)/2),int((len(data[0])-1)/2))  
for _ in range(10000000):
    c = kaart[pos]
    if c == '.':
        d = left[d]
        kaart[pos] = 'w'
    elif c == 'w':
        kaart[pos] = '#'
        cnt += 1
    elif c == '#':
        kaart[pos] = 'f'
        d = right[d]
    elif c == 'f':
        dr,dc = d
        d = (-dr,-dc)
        kaart[pos] = '.'
    r,c = pos; dr,dc = d
    pos = (r+dr,c+dc)

print(cnt)