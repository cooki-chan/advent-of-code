input = open('day6/inp.txt').read().split('\n')

roblox = []
pos = [0,0,0]

for row, i in enumerate(input):
    for col, j in enumerate(i):
        if j == "#":
            roblox.append((row, col))
        if j == "^":
            pos = [row, col, 0]

record = [(pos[0], pos[1])]
orgPos = pos.copy()

while (not (pos[0], pos[1]) == orgPos) and (pos[0] < len(input)) and (pos[1] < len(input[0]))  and (pos[0] >= 0) and (pos[1] >= 0):
    record.append((pos[0], pos[1]))
    print(pos)

    tempPos = pos.copy()
    match pos[2]:
        case 0:
            tempPos[0]-=1
        case 90:
            tempPos[1]+=1
        case 180:
            tempPos[0]+=1
        case 270:
            tempPos[1]-=1

    if (tempPos[0], tempPos[1]) in roblox:
        pos[2] +=90
        if pos[2] > 270:
            pos[2] = 0
        continue


    match pos[2]:
        case 0:
            pos[0]-=1
        case 90:
            pos[1]+=1
        case 180:
            pos[0]+=1
        case 270:
            pos[1]-=1


new_rec = []
for i in record:
    if not i in new_rec:
        new_rec.append(i)

print(len(new_rec))
#print(new_rec)