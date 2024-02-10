data = open('in16').read().strip().split(',')
program = 'abcdefghijklmnop'

def dance(program):
    for i in data:
        if i[0] == 's':
            idx = int(i[1:])
            program = program[-idx:]+program[:-idx]
        if i[0] == 'x':
            a,b = i[1:].split('/')
            ca = program[int(a)]
            cb = program[int(b)]
            program = list(program)
            program[int(b)] = ca
            program[int(a)] = cb
            program = ''.join(program)
        if i[0] == 'p':
            a,b = i[1:].split('/')
            ida = program.index(a)
            idb = program.index(b)
            program = list(program)
            program[idb] = a
            program[ida] = b
            program = ''.join(program)
    return program

print(dance(program))

dances = []
i = 0
while i < 1e9:
    program = dance(program)
    if program in dances:
        idp = dances.index(program)
        rep = i-idp
        while i < 1e9:
            i += rep
        i-=rep
    dances.append(program)
    i += 1

print(program)