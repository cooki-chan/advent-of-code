input = open('day19/inp.txt').read().split('\n\n')

towels = input[0].split(", ")
towels.sort(key=len)
designs = [i for i in input[1].split("\n")]

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

longestCombo = designs.copy()
longestCombo.sort(key=len, reverse=True)
longestCombo = len(longestCombo[0])

change = True
combos = set(towels.copy())
finished = set()

iters = 1
while change:
    print(iters)
    change = False
    new = set()

    for t in towels:
        for c in combos:
            if len(c+t) < longestCombo:
                change = True
                new.add(c+t)
            finished.add(c)
    
    combos = new
    iters +=1

    print(longestCombo)
    print(len(combos))