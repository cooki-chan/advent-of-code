import math


input = open('day14/inp.txt').read().split('\n')

reactions = {"ORE":[[1, "ORE"], 1]}
oreConversions = {}

for i in input:
    r = i.split(" => ")
    if "ORE" not in r[0]:
        result = (int(r[1].split(" ")[0]), r[1].split(" ")[1])
        reactants = [[int(i.split(" ")[0]), i.split(" ")[1]] for i in r[0].split(", ")]
        reactions[result[1]] = [reactants, result[0]]
    else:
        result = (int(r[1].split(" ")[0]), r[1].split(" ")[1])
        reactants = [[int(i.split(" ")[0]), i.split(" ")[1]] for i in r[0].split(", ")]
        oreConversions[result[1]] = [reactants[0][0], result[0]]

mats = {"FUEL":1}
leftovers = {}
for i in reactions:
    leftovers[i] = 0
for i in oreConversions:
    leftovers[i] = 0

while True:
#for _ in range(10):
    new = {}
    print(mats)
    print(leftovers)

    changed = False
    for i in mats:
        if i in reactions:
            div = reactions[i][1]
            for j in reactions[i][0]:
                print(new, i)
                if j[1] not in new:
                    new[j[1]] = 0

                new[j[1]] += ((j[0]) * math.ceil(mats[i]/div)) - leftovers[j[1]]

                if new[j[1]] < 0:
                    new[j[1]] -= ((j[0]) * math.ceil(mats[i]/div)) - leftovers[j[1]]
                    leftovers[j[1]] -= ((j[0]) * mats[i]/div)

                else:
                    leftovers[j[1]] = 0
                    leftovers[i] = mats[i] % div

                changed = True
        else:
            if i not in new:
                new[i] = mats[i]
            else:
                new[i] += mats[i]
    mats = new
    
    if new.keys() == oreConversions.keys():
        break

print(mats, oreConversions)

ores = 0
for i in mats:
    ores += oreConversions[i][0]*  math.ceil(mats[i] / oreConversions[i][1])
print(ores)
print(leftovers)
