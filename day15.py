A,B = [int(i.split()[-1]) for i in open('in15').read().strip().split('\n')]
print(A,B)
# af = 16807;bf = 48271
# p = 2147483647

def ga(x):return (x*16807)%2147483647
def gb(x):return (x*48271)%2147483647

cnt = 0
for i in range(40000000):
    A = ga(A)
    B = gb(B)
    if bin(A)[-16:] == bin(B)[-16:]:
        cnt += 1

A = 65
print(cnt)
A,B = [int(i.split()[-1]) for i in open('in15').read().strip().split('\n')]
cnt = i = 0
# A= 65;B = 8921
while i < 5e6:
    A = ga(A);B = gb(B)
    while A%4 != 0:
        A = ga(A)
    while B%8 != 0:
        B = gb(B)
    if bin(A)[-16:] == bin(B)[-16:]:
        cnt += 1
    i+=1
print(cnt)

#too low 297