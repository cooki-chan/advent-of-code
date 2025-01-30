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
            return 99999999999
        else:
            return -99999999999

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