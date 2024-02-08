data = open('in1').read().strip()
print(data)
res = 0
c = data[-1]
for i in data:
    if i == c:
        res += int(i)
    c = i

print(res)

res = 0
l = len(data)

for i,val in enumerate(data):
    if val == data[(i+int(l/2))%l]:
        res += int(data[i])

print(res)