import math


class Node:
    def __init__(self, type) -> None:
        self.type = type
        match type:
            case "|":
                self.connect = ["N", "S"]
            case "-":
                self.connect = ["E", "W"]
            case "L":
                self.connect = ["N", "E"]
            case "J":
                self.connect = ["N", "W"]
            case "7":
                self.connect = ["S", "W"]
            case "F":
                self.connect = ["S", "E"]
            case ".":
                self.connect = []
            case "S":
                self.connect = []
        pass

inp = open('day10/inp.txt').read().split("\n")
input = []
sX = 0
sY = 0

for x, i in enumerate(inp):
    temp = []
    for y, j in enumerate(i):
        temp.append(Node(j))
        if j == "S":
            sX = y
            sY = x
    input.append(temp)

def followPipe(pipes, posX, posY, turnDir, length):
    visited = [(sX, sY)]
    node = pipes[posY][posX]
    length = 0
    while pipes[posY][posX].connect != []:
        visited.append((posX, posY))
        node = pipes[posY][posX]
        connections = node.connect
        connections.remove(turnDir)
        match connections[0]:
            case "N":
                posY-=1
                turnDir = "S"
            case "S":
                posY+=1
                turnDir = "N"
                
            case "W":
                posX-=1
                turnDir = "E"
            case "E":
                posX+=1
                turnDir = "W"
    return visited

def clearTrash(map, goodPoints):
    for i, row in enumerate(map):
        for j, col in enumerate(row):
            if not (j, i) in goodPoints:
                map[i][j] = Node(".")

def lineSweep(map):
    output = 0
    for i, row in enumerate(map):
        record = False
        halfTrigger = False
        for j, col in enumerate(row):
            if map[i][j].type in "|LJS":
                record = not record

            if record and map[i][j].type == ".":
                output+=1
                print(f"{i}, {j}")
    return output

                

N = input[sY-1][sX]
S = input[sY+1][sX]
E = input[sY][sX+1]
W = input[sY][sX-1]
temp = input[sY][sX]

visitedPoints = []
if N.type in "|F7":
    visitedPoints = followPipe(input, sX, sY-1, "S",0)
elif S.type in "|LJ":
    visitedPoints = followPipe(input, sX, sY+1, "N",0)
elif E.type in "-J7":
    visitedPoints = followPipe(input, sX+1, sY, "W",0)
elif W.type in "-LF":
    visitedPoints = followPipe(input, sX-1, sY, "E",0)
else:
    print("FUCK")

clearTrash(input, visitedPoints)
for i in input:
    outpit = ""
    for j in i:
        outpit += j.type
    print(outpit)
print(lineSweep(input))



