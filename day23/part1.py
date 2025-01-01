input = open('day23/inp.txt').read().split('\n')

connections = {}

for i in input:
    one = i[:2]
    two = i[3:]

    if one in connections.keys():
        connections[one].append(two)
    else:
        connections[one] = [two]

    if two in connections.keys():
        connections[two].append(one)
    else:
        connections[two] = [one]

thre = set()

for i in connections:
    for j in connections[i]:
        sim = set()
        for k in connections[j]:
            if k in connections[i]:
                sim.add(k)
        #print(sim)

        for k in sim:
            thre.add(frozenset({i, j, k}))
            #print((i, j, k))

out = 0
for i in thre:
    add = False
    for j in i:
        if "t" == j[0]:
            add = True
    if add:
        out+=1

print(connections)