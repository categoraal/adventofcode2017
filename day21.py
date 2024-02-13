data = open('in21').read().strip().split('\n')

def rotate90(x): return tuple(zip(*reversed(x)))
def flip(x): return tuple(tuple(reversed(i)) for i in x)

mapping = {}
for i in data:
    a,b = [j.split('/') for j in i.split(' => ')]
    a = [list(i) for i in a]
    for _ in range(4):
        a = rotate90(a)
        f = flip(a)
        mapping[a] = b
        mapping[f] = b
        
def enhance(x):
    n = 2 if len(x)%2 == 0 else 3
    subpattern = []
    for i in range(int(len(x)/n)):
        row = []
        crow = x[n*i:n*(1+i)]
        for j in range(int(len(x)/n)):
            block = tuple([tuple(k[n*j:n*(1+j)]) for k in crow])
            row.append(mapping[block])
        subpattern += [''.join(i) for i in zip(*row)]
    return subpattern

for part in [5,18]:
    pattern = ['.#.','..#','###']
    for _ in range(part):
        pattern = enhance(pattern)
    print(sum([i.count('#') for i in pattern]))