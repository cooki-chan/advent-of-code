input = open('day19/inp.txt').read().split('\n\n')

towels = input[0].split(", ")
towels.sort(key=len)
print(len(towels))
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
        

reduced = list(remover)
for t in betterTowels:
    if t in remover or not len(t) == t.count("."):
        reduced.append(towels[betterTowels.index(t)])

reduced.sort(key=len, reverse=True)
towels = reduced

def replacements(design, rep):
    splits = design.split(rep)

    reps = [splits.pop(0)]

    for i in splits:
        newR = []
        for r in reps:
            newR.append(r + rep + i)
            newR.append(r + "." + i)
        reps = newR
    
    return reps


prelimSum = 0
for d in designs:
    s = 0
    for i in remover:
        s+= d.count(i)
    if s == len(d):
        prelimSum+=1
        designs.remove(d)

print(len(towels))
print(towels)
towels = list(set(towels))

new = []
for indd, d in enumerate(designs):
    #print(d)
    pos = [d]
    for t in towels:
        #print(t)
        te = []
        for p in pos:

            if t in p:
                if t in remover:
                    for ind, po in enumerate(pos):
                        pos[ind] = po.replace(t, ".")
                else:
                    #print(len(te))
                    te += replacements(p, t)
                    te = list(set(te))
                    #print(len(te))
        pos += te
        pos = list(set(pos))

        tt = []
        for p in pos:
            tt.append(p.replace(".", ""))
        if "" in tt:
            break
            
    
    clean = []
    for i in pos:
        clean.append(i.replace(".", ""))
        
    if "" in clean:
        new.append(True)
        print(indd)
        print(d)
    else:
        new.append(False)


print(new.count(True))

# 4
# uubuggugwrgubbwguugbuubwugugbwwwgbrbuggbbrrgbrguwuuurggbg
# 161
# gbrgrwbbbuwuuwwgbubbrguwrrgwwgwubbbrubgburggg
# 178
# rgrggwwugwwgbgruwgrrubrgbgbubbugwwgrurgwubr
# 227
# buugrgrbrrwbrbrrwuurgrbrgbrgburgggbwburgrwggrgrbuubbbbb
# 230
# wguuwguugbrgwbgrgbgwbguugwwbrgbgbbbwwbuuuuguuwubbwgggg
# 242
# uubbrwururuuuggwuwgbbbgbwbgwgwbbuwwbbgbrbbbwubr
# 244
# brbuuuwugrrguburrgwuugwbbrggrgrgguguguwbrwbwbbwwugguwwwu
# 270
# ugbwbuuburgrugwrggbrrgugwbrbbbrwwbgrgggbbwbubbgggrgguugu
# 334
# buuwbwwbrwbgubugwbrgrgwwuwgubgwurguggbgguugbrrrr