input = ""
with open('day14/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

walls = {}
lowestY = 0

for i in input: #wall setup
    positions = i.split(" -> ")
    for j in range(len(positions)-1):
        pos1 = positions[j].split(",")
        pos2 = positions[j+1].split(",")
        for i in range(len(pos1)):
            pos1[i] = int(pos1[i])
            pos2[i] = int(pos2[i])
            
        if not pos1[0] == pos2[0]: #x-coord changing
            start = pos1[0]
            if pos2[0] < start:
                start = pos2[0]

            for i in range(abs(pos1[0]-pos2[0])+1):
                if start+i in walls.keys():
                    walls[start+i].append(pos1[1])
                else:
                    walls[start+i] = [pos1[1]]

        elif not pos1[1] == pos2[1]: #y-coord changing
            start = pos1[1]
            if pos2[1] < start:
                start = pos2[1]

            for i in range(abs(pos1[1]-pos2[1])+1):
                if pos1[0] in walls.keys():
                    walls[pos1[0]].append(start+i)
                else:
                    walls[pos1[0]] = [start+i]
                if start+i > lowestY:
                    lowestY = start+i

stillFalling = True
noSand = 0
sand = []
while stillFalling:
    yCoord = 0
    xCoord = 500
    while not yCoord in walls[500]:
        yCoord+=1
    yCoord-=1

    while True:
        if not xCoord+1 in walls.keys():
            walls[xCoord+1] = []
        if not xCoord-1 in walls.keys():
            walls[xCoord-1] = []

        if yCoord+1 == lowestY+2:
            yCoord+1
            break
        if not yCoord+1 in walls[xCoord]: #straight down
            yCoord+=1
        elif not yCoord+1 in walls[xCoord-1]: #left check
            xCoord-=1
            yCoord+=1
        elif not yCoord+1 in walls[xCoord+1]: #right check
            xCoord+=1
            yCoord+=1
        else:
            break

    if stillFalling:
        if xCoord in walls.keys():
            walls[xCoord].append(yCoord)
        else:
            walls[xCoord] = [start+i]
        sand.append((xCoord, yCoord))
        noSand+=1
    if yCoord <= 0:
        stillFalling = False
    print((xCoord, yCoord))

print(noSand)
        


    


