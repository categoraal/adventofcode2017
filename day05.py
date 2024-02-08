data = [int(i) for i in open('in5').read().strip().split('\n')]

p = c=  0
while p < len(data):
    np = p+data[p]
    data[p] += 1
    p = np
    c += 1

print(c)

data = [int(i) for i in open('in5').read().strip().split('\n')]

p = c=  0
while p < len(data):
    np = p+data[p]
    if data[p] >= 3:
        data[p] -= 1
    else:
        data[p] += 1
    p = np
    c += 1

print(c)