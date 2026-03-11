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
        dists.append((i, j, dist(i, j)))

dists.sort(key= lambda x: x[2])
dists = dists[0:1000]
circuts = []

print(dists)
for i in dists:
    #print(circuts)
    p1set = None
    p2set = None

    for ind, j in enumerate(circuts):
        if i[0] in j:
            p1set = ind
        if i[1] in j:
            p2set = ind
    
    print(i, p1set, p2set)
    if p1set == None and p2set != None:
        circuts[p2set].add(i[0])
        print(1)
        continue

    if p1set != None and p2set == None:
        circuts[p1set].add(i[1])
        print(2)
        continue

    if p1set == p2set and p1set != None:
        print(3)
        continue

    if p1set != None and p2set != None:
        circuts[p1set] = circuts[p1set] | circuts[p2set]
        circuts.remove(circuts[p2set])
        print(4)
        continue

    if p1set == None and p2set == None:
        new = set()
        new.add(i[0])
        new.add(i[1])
        circuts.append(new)
        print(5)
        continue

out = set()
for i in circuts:
    #print(i)
    out.add(len(i))
out = list(out)
out.sort(reverse=True)
print(out)
o = 1
for i in out[0:3]:
    o *=  i
print(o)