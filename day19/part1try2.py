input = open('day19/inp.txt').read().split('\n\n')

towels = input[0].split(", ")
towels.sort(key=len)
designs = [i for i in input[1].split("\n")]

byLen = {}
for t in towels:
    print(t)
    if len(t) in byLen:
        byLen[len(t)].append(t)
    else:
        byLen[len(t)] = [t]

remover = set()
betterTowels = towels.copy()
for l in range(1, len(towels[-1])+1):
    for checking in byLen[l]:
        for checked in betterTowels:
            if checking in checked:
                betterTowels[betterTowels.index(checked)] = checked.replace(checking, ".")
                
                if len(checked.replace(checking, ".")) == checked.replace(checking, ".").count("."):
                    remover.add(checking)
        

sigChars = set()
reduced = list(remover)
for t in betterTowels:
    for c in t:
        sigChars.add(c)

    if t in remover or not len(t) == t.count("."):
        reduced.append(towels[betterTowels.index(t)])

sigChars.remove(".")

reduced.sort(key=len, reverse=True)
towels = reduced

print(towels)

out = []
for d in designs:
    
    for t in towels:
        d = d.replace(t, ".")
    out.append(d)

outt = 0
for ind, o in enumerate(out):
    if len(o) == o.count("."):
        print(ind)
        print(designs[ind])
        outt+=1
print(outt)