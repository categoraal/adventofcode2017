data = int(open('in3').read().strip())
i = 1
while i**2 < data:
    i+=2

print('squared number',i)
for k in range(1,5):
    if i**2-(i-1)*k < data <= i**2-(i-1)*(k-1):
        print(int(abs(((i**2-(i-1)*k)+(i**2-(i-1)*(k-1)))/2-data)+i//2))


# part 2
nums = {(0,0):1}
num = 1
i = 1
x = y = 0
f = False

def addnum(x,y):
    res = 0
    for dx in (-1,0,1):
        for dy in (-1,0,1):
            if (x+dx,y+dy) in nums:
                res += nums[(x+dx,y+dy)]
    return res


while num < data:
    for dx,dy in ((0,1),(-1,0)):
        for _ in range(i):
            if f:
                continue
            x += dx;y+=dy
            num = addnum(x,y)
            nums[(x,y)] = num
            if num > data:
                f = True
                print(num)
                break
        if f:
            break
    i+=1
    for dx,dy in ((0,-1),(1,0)):
        for _ in range(i):
            if f:
                continue
            x += dx; y += dy
            num = addnum(x,y)
            nums[(x,y)] = num
            if num > data:
                f = True
                print(num)
                break
        if f:
            break
    i += 1