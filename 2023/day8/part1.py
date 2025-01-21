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

currPos = "AAA"
instructionIndex = 0
noMoves = 0
while currPos != "ZZZ":
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

print(noMoves)

