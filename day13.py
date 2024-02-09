data = [[int(j) for j in i.split(': ')] for i in open('in13').read().strip().split('\n')]
print(data)

def severity(data,offset):
    res = 0
    p2 = 0
    for t,d in data:
        if (t+offset)%(2*d-2) == 0:
            # print(t,d)
            res += t*d
            p2 += 1
    return res,p2

print(severity(data,0)[0])

i = 0
while severity(data,i)[1] > 0:
    i += 1

print(i)