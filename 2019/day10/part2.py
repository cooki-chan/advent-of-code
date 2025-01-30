input = open('day10/inp.txt').read().split('\n')

nodes = []

for row, i in enumerate(input):
    for col, j in enumerate(i):
        if j == "#":
            nodes.append([row, col])

def ang(n1, n2):
    try:
        return round((n1[0] - n2[0]) / (n1[1] - n2[1]), 5)
    except ZeroDivisionError:
        if n1[0] > n2[0]:
            return -999999999999
        else:
            return 99999999999

max = 0
cu = -1
for curr in nodes:
    l = set()
    r = set()

    for i in nodes:
        if i == curr:
            continue
        
        if curr[1] > i[1]:
            l.add(ang(curr, i))
        else:
            r.add(ang(curr, i))
    print(len(l) + len(r), curr)
    if len(l) + len(r) > max:
        max = len(l) + len(r)
        cu = curr
print(max, cu)

def dist(n1, n2):
    return abs(n1[0] - n2[0]) + abs(n1[1] - n2[1])

curr = cu
l = {}
r = {}

for i in nodes:
    a = ang(curr, i)
    if curr[1] > i[1]:
        if a not in l:
            l[a] = []
        l[a].append(i)
    else:
        if a not in r:
            r[a] = []
        r[a].append(i)
print(l)

removed = []
while len(removed) <= 200:
    right_elim = list(r.keys())
    right_elim.sort()
    
    for i in right_elim:
        closest = []
        m  = 1000000
        for j in r[i]:
            if dist(curr, j) < m:
                m = dist(curr, j)
                closest = j
        if not closest == []:
            removed.append(j.copy())
            r[i].remove(j)

    left_elim = list(l.keys())
    left_elim.sort()
    
    for i in left_elim:
        closest = []
        m  = 1000000
        for j in l[i]:
            if dist(curr, j) < m:
                m = dist(curr, j)
                closest = j
        if not closest == []:
            removed.append(j.copy())
            l[i].remove(j)

print(removed[199][1] * 100 + removed[199][0])