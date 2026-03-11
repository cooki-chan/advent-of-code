input = open('08/inp.txt').read().split('\n')

boxes = [tuple(map(int, i.split(","))) for i in input]
dists = []

def dist(i, j):
    out = 0
    for d in range(len(i)):
        out += (i[d] - j[d]) ** 2
    return out ** 0.5

for i in boxes:
    for j in boxes[boxes.index(i)+1:]:
        dists.append((i, j))

dists.sort(key= lambda x: dist(x[0], x[1]))
circuts = []
seen = set()

#print(dists)
for i in dists:
    p1set = None
    p2set = None

    seen.add(i[0])
    seen.add(i[1])

    #print("CICUTS", circuts)

    for ind, j in enumerate(circuts):
        if i[0] in j:
            p1set = ind
        if i[1] in j:
            p2set = ind
    
    #print(i, p1set, p2set)
    if p1set == None and p2set != None:
        circuts[p2set].add(i[0])

    if p1set != None and p2set == None:
        circuts[p1set].add(i[1])

    if p1set != None and p2set != None and p1set != p2set:
        circuts[p1set] = circuts[p1set] | circuts[p2set]
        circuts.pop(p2set)

    if p1set == None and p2set == None:
        new = set()
        new.add(i[0])
        new.add(i[1])
        circuts.append(new)

    if(len(circuts) == 1 and len(seen) == len(boxes) == len(circuts[0])):
        for ind, k in enumerate(dists):
            if k[0][0] == i[0][0] and k[1][0] == i[1][0]:
                print(ind, k)

        print("LOOK PAPA! IVE GOT ABNS ANSWERT!! YAY: ", i[0][0] * i[1][0])
        break

    if p1set == p2set and p1set != None:
        pass