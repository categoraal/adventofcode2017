data = open('in19').read().split('\n')[:-2]

queue = [(0,data[0].index('|'))]
res = ''
d = (1,0)
cnt = 0
for r,c in queue:
    seg = data[r][c]
    if seg == ' ':
        break

    if seg not in '-|+':
        res += seg
    
    if seg == '+':
        for nd in ((-dc,dr),(dc,-dr)):
            dr,dc = nd
            nr = r+dr;nc = c+dc
            if 0 <= nr < len(data) and 0<=nc<len(data[0]) and data[nr][nc] != ' ':
                d = nd

    dr,dc = d
    nr = r+dr;nc = c+dc
    if 0<=nr<len(data) and 0<=nc<len(data[0]):
        queue.append((nr,nc))
        cnt += 1

print(res)
print(cnt)

            