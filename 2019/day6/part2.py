input = open('day6/inp.txt').read().split('\n')

orbits = {}
changes = [1,2]
while changes:

    for i in input:
        con = i.split(")")
        if con[0] not in orbits:
            orbits[con[0]] = set()

        if con[1] not in orbits[con[0]]:
            orbits[con[0]].add(con[1])
            orbits[con[1]] = set()

        if con[1] in orbits:
            old = orbits[con[0]].copy()
            orbits[con[0]] = orbits[con[0]].union(orbits[con[1]])


    #print(orbits)
    out = 0
    for i in orbits:
        out += len(orbits[i])
    changes.append(out)
    if changes[-2] == changes[-1]:
        break
    #print(changes)

#YOU to SAN
pos = "YOU"

traveledYOU = 0
path = []
while "SAN" not in orbits[pos]:
    for i in input:
        if ")" + pos in i:
            pos = i.split(")")[0]
            traveledYOU+=1
            path.append(pos)
            break

#SAN to YOU
pos = "SAN"

traveledSAN = 0
path2 = []
while "YOU" not in orbits[pos]:
    for i in input:
        if ")" + pos in i:
            pos = i.split(")")[0]
            traveledSAN+=1
            path2.append(pos)
            break

print(traveledSAN + traveledYOU - 2)