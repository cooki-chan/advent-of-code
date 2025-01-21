def check(arr):
    fail = False
    for j in arr:
        if j in lib.keys():
            for k in lib[j]:
                if k in arr[0:arr.index(j)]:
                    fail = True
    return fail

def flat (arr):
    return list(set(arr))



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
pain = []
for lo in upd:
    fail = check(lo)
    
    if fail:
        new = [lo[0]]
        for i in lo[1:len(lo)]:
            for j in range(len(new)):
                temp = new.copy()
                temp.insert(j,i)
                f = check(temp)
                if not f:
                    new = temp
                    break
            if not i in new:
                new.append(i)
                
        pain.append(new)
        #print(new)

for i in pain:
    temp = []
    for j in i:
        if not j in temp:
            temp.append(j)
    out += temp[int(len(temp)/2)]
print(out)