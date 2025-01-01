input = open('day19/inp.txt').read().split('\n\n')

towels = input[0].split(", ")
towels.sort(key=len)
designs = [i for i in input[1].split("\n")]

#print(towels)


byLen = {}
for t in towels:
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
        

reduced = list(remover)
for t in betterTowels:
    if t in remover or not len(t) == t.count("."):
        reduced.append(towels[betterTowels.index(t)])

print(remover)
print(len(reduced))
print(len(towels))

reduced.sort(key=len)
towels = reduced
