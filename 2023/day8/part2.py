class node:
    def __init__(self, left, right) -> None:
        self.left = left
        self.right = right
        pass    

input = open('day8/inp.txt').read().split("\n")

instructions = input[0]

input.pop(0)
input.pop(0)

paths = {}

for i in input:
    pos = i.split(" = ")[0]
    left = i.split(" = ")[1].split(", ")[0][1:]
    right = i.split(" = ")[1].split(", ")[1][:3]
    paths[pos] = node(left, right)

startPos = []
for i in paths.keys():
    if i[2] == "A":
        startPos.append(i)
noMovesFinal = []

for i in startPos:
    currPos = i
    instructionIndex = 0
    noMoves = 0
    while currPos[2] != "Z":
        currIns = instructions[instructionIndex]
        pos = paths[currPos]

        if currIns == "R":
            currPos = pos.right
        else:
            currPos = pos.left
        
        instructionIndex+=1
        if instructionIndex == len(instructions):
            instructionIndex = 0
        noMoves +=1
    noMovesFinal.append(noMoves)


noMovesFinal.sort(reverse=True)
gcf = 0
for j in range(1, noMovesFinal[0]):
    allGCF = True
    for i in noMovesFinal:
        if i % j != 0:
            allGCF = False
    if(allGCF):
        gcf = j

out = 1
for i in noMovesFinal:
    out *= i
    out /= gcf
print(out * gcf)

