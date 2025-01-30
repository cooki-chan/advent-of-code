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



print(changes[-1])