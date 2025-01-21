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

def deb():
    strin = ""
    for row in range(len(map)):
        for col in range(len(map[0])):
            if (row, col) in boxes:
                strin += "O"
            elif (row, col) in walls:
                strin+="#"
            elif [row, col] == rob:
                strin+="@"
            else:
                strin+="."
            
        strin+="\n"
    print(strin)

def moveBox(row, col, direction):
    global walls
    global boxes
    global rob

    tR = row
    tC = col
    new = []
    tB = boxes.copy()
    save = []
    while (tR, tC) in boxes and (tR, tC) not in walls:
        # print(tR)
        # print(tC)
        save.append((tR, tC))
        boxes.remove((tR, tC))
        match direction:
            case "^":
                tR-=1
            case ">":
                tC+=1
            case "v":
                tR+=1
            case "<":
                tC-=1
        # print(tR)
        # print(tC)
        new.append((tR, tC))

    if (tR, tC) in walls:
        boxes+=save
        return
    # print(new)
    # print(boxes)
    # print(tB)
    boxes+=new
    
    match direction:
        case "^":
            rob[0]-=1
        case ">":
            rob[1]+=1
        case "v":
            rob[0]+=1
        case "<":
            rob[1]-=1

for row, i in enumerate(map):
    for col, j in enumerate(i):
        match j:
            case "#":
                walls.append((row, col))
            case "O":
                boxes.append((row, col))
            case "@":
                rob = [row, col]

for i in instructions:
    match i:
        case "^":
            if (rob[0]-1, rob[1]) in walls:
                continue
            elif (rob[0]-1, rob[1]) in boxes:
                moveBox(rob[0]-1, rob[1], i)
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
            else:
                rob[0]+=1

        case "<":
            if (rob[0], rob[1]-1) in walls:
                continue
            elif (rob[0], rob[1]-1) in boxes:
                moveBox(rob[0], rob[1]-1, i)
            else:
                rob[1]-=1

out = 0
for i in boxes:
    out += 100 * i[0]
    out += i[1]
deb()
print(out)
