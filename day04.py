data = [i.split() for i in open('in4').read().strip().split('\n')]

p1 = 0
p2 = 0
for row in data:
    if len(row) == len(set(row)):
        p1 += 1
    l = [''.join(sorted(list(i))) for i in row]
    if len(row) == len(set(l)):
        p2+=1
print(p1)
print(p2)