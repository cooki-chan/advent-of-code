input = open('day11/inp.txt').read().split("\n")

def distance(gal1, gal2):
    return abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1])

gals = []
blankRows = 0
for y, i in enumerate(input):
    blankRow = True
    count = 0
    for x, j in enumerate(i):
        if j == "#":
            count +=1
            gals.append([x, y+blankRows])
            blankRow = False
    if blankRow:
        blankRows+=1

colsWGals = []
for i in gals:
    colsWGals.append(i[0])
colsWGals = set(colsWGals)

colsWOGals = []
for i in range(len(input[0])):
    if not i in colsWGals:
        colsWOGals.append(i)

for x, i in enumerate(gals):
    blankColsBefore = 0
    for j in colsWOGals:
        if i[0] > j:
            blankColsBefore+=1
    gals[x] = [i[0]+blankColsBefore, i[1]]

out = 0
count = 0
while gals != []:
    for i in range(len(gals)-1):
        count+=1
        out += distance(gals[0], gals[i+1])
    gals.pop(0)

print(out)