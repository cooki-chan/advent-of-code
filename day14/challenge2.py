input = ""
with open('day14/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

walls = []
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
                walls.append((start+i, pos1[1]))

        elif not pos1[1] == pos2[1]: #y-coord changing
            start = pos1[1]
            if pos2[1] < start:
                start = pos2[1]

            for i in range(abs(pos1[1]-pos2[1])+1):
                walls.append((pos1[0], start+i))
                if start+i > lowestY:
                    lowestY = start+i

stillFalling = True
noSand = 0
sand = []
while stillFalling:
    yCoord = 0
    xCoord = 500
    while not (500, yCoord) in walls:
        yCoord+=1
    yCoord-=1

    while True:
        if yCoord+1 == lowestY+1:
            yCoord+1
            break
        if not (xCoord, yCoord+1) in walls: #straight down
            yCoord+=1
        elif not (xCoord-1, yCoord+1) in walls: #left check
            xCoord-=1
            yCoord+=1
        elif not (xCoord+1, yCoord+1) in walls: #right check
            xCoord+=1
            yCoord+=1
        else:
            break

    if stillFalling:
        walls.append((xCoord, yCoord))
        sand.append((xCoord, yCoord))
        noSand+=1
    if yCoord == 0:
        stillFalling == False
    print((xCoord, yCoord))

print(noSand)
        


    


