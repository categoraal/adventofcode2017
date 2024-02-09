data = [int(i) for i in open('in6').read().strip().split()]

seen = [tuple(data)]
c = 1
repetition = False
while repetition == False:
    idx = data.index(max(data))
    blocks = data[idx]
    data[idx] = 0
    for i in range(blocks):
        data[(idx+i+1)%len(data)] += 1
    if tuple(data) in seen:
        print(c)
        repetition = True
        print(len(seen)-seen.index(tuple(data))) 
    seen.append(tuple(data))
    c += 1