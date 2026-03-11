input = open('07/inp.txt').read().split('\n')
#input = open('07/ex_inp.txt').read().split('\n')


tach = []
for row, i in enumerate(input):
    for col, j in enumerate(i):
        if j == "^":
            tach.append((row, col))

sp = 0
q = [(0, input[0].index("S"))]
old = []
while q != []:
    print(q)
    l = q.pop(0)
    if l in old or l[0]+1 >= len(input):
        continue
    if (l[0]+1, l[1]) in tach:
        q.append((l[0]+1, l[1]-1))
        q.append((l[0]+1, l[1]+1))
        sp +=1
    else:
        q.append((l[0]+1, l[1]))
    old.append(l)

print(sp)