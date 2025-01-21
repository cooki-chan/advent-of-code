input = open('day5/inp.txt').read().split('\n')

lib = {}
upd = []

for i in input:
    if not "," in i and not i == "":
        l = int(i.split("|")[0])
        r = int(i.split("|")[1])

        if l in lib.keys():
            lib[l].append(r)
        else:
            lib[l] = [r]
    else:
        if not i == "":
            upd.append([int(item) for item in i.split(",")])

out = 0
for lo in upd:
    fail = False
    for j in lo:
        if j in lib.keys():
            for k in lib[j]:
                if k in lo[0:lo.index(j)]:
                    fail = True
    
    if not fail:
        out += lo[int(len(lo)/2)]

print(out)
