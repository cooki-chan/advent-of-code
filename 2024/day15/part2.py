import time

input = open('day15/inp.txt').read().split("\n\n")

map = [i for i in input[0].split("\n")]
instructions = "".join(input[1].split("\n"))
print(instructions)

global walls
walls = []

global boxes
boxes = []

global rob
rob = []

for row, i in enumerate(map):
    for col, j in enumerate(i):
        match j:
            case "#":
                walls.append((row, col*2))
                walls.append((row, col*2+1))
            case "O":
                boxes.append((row, col*2))
            case "@":
                rob = [row, col*2]

def deb():
    strin = ""
    for row in range(len(map)):
        pas = False
        for col in range(len(map[0])*2):
            if pas:
                pas = False
                continue
            if (row, col) in boxes:
                strin += "[]"
                pas = True
            elif (row, col) in walls:
                strin+="#"
            elif [row, col] == rob:
                strin+="@"
            else:
                strin+="."
            
        strin+="\n"
    print(strin)

deb()

def moveBox(row, col, direction):
    global walls
    global boxes
    global rob


    if direction in "<":
        tempCol = col
        removed = []
        while (row, tempCol) in boxes:
            removed.append((row, tempCol))
            tempCol-=2
        if (row, tempCol) in walls and (row, tempCol+1) in walls:
            return
        for i in removed:
            boxes.remove(i)
            boxes.append((i[0], i[1]-1))

    elif direction in ">":
        tempCol = col
        removed = []
        while (row, tempCol) in boxes:
            removed.append((row, tempCol))
            tempCol+=2
        if (row, tempCol) in walls:
            return
        for i in removed:
            boxes.remove(i)
            boxes.append((i[0], i[1]+1))

    elif direction in "^":
        boxesChecked = []
        needChecking = [(row, col)]
        while not needChecking == []:
            for i in needChecking:
                if i in boxesChecked:
                    needChecking.remove(i)
                    continue
                sus = [(i[0]-1, i[1]-1), 
                        (i[0]-1, i[1]), 
                        (i[0]-1, i[1]+1)]
                
                for j in sus:
                    if j in boxes:
                        needChecking.append(j)

                sus.remove(sus[0])

                for j in sus:
                    if j in walls:
                        return
                    
                needChecking.remove(i)
                boxesChecked.append(i)

        for i in boxesChecked:
            boxes.remove(i)
            boxes.append((i[0]-1, i[1]))

    elif direction in "v":
        boxesChecked = []
        needChecking = [(row, col)]
        while not needChecking == []:
            for i in needChecking:
                if i in boxesChecked:
                    needChecking.remove(i)
                    continue
                sus = [(i[0]+1, i[1]-1), 
                        (i[0]+1, i[1]), 
                        (i[0]+1, i[1]+1)]
                
                for j in sus:
                    if j in boxes:
                        needChecking.append(j)

                sus.remove(sus[0])

                for j in sus:
                    if j in walls:
                        return
                
                print(needChecking)
                needChecking.remove(i)
                boxesChecked.append(i)

        for i in boxesChecked:
            boxes.remove(i)
            boxes.append((i[0]+1, i[1]))
    
    match direction:
        case "^":
            rob[0]-=1
        case ">":
            rob[1]+=1
        case "v":
            rob[0]+=1
        case "<":
            rob[1]-=1

for i in instructions:
    # deb()
    # print(i)
    match i:
        case "^":
            if (rob[0]-1, rob[1]) in walls:
                continue
            elif (rob[0]-1, rob[1]) in boxes:
                moveBox(rob[0]-1, rob[1], i)
            elif (rob[0]-1, rob[1]-1) in boxes:
                moveBox(rob[0]-1, rob[1]-1, i)
            else:
                rob[0]-=1

        case ">":
            if (rob[0], rob[1]+1) in walls:
                continue
            elif (rob[0], rob[1]+1) in boxes:
                moveBox(rob[0], rob[1]+1, i)
            else:
                rob[1]+=1

        case "v":
            if (rob[0]+1, rob[1]) in walls:
                continue
            elif (rob[0]+1, rob[1]) in boxes:
                moveBox(rob[0]+1, rob[1], i)
            elif (rob[0]+1, rob[1]-1) in boxes:
                moveBox(rob[0]+1, rob[1]-1, i)
            else:
                rob[0]+=1

        case "<":
            if (rob[0], rob[1]-1) in walls:
                continue
            elif (rob[0], rob[1]-2) in boxes:
                moveBox(rob[0], rob[1]-2, i)
            elif (rob[0], rob[1]-1) in boxes:
                print("HOLY FUCK YO")
                break
            else:
                rob[1]-=1
    #time.sleep(1)

out = 0
for i in boxes:
    out += 100 * i[0]
    out += i[1]
deb()
print(out)