input = ""
with open('day12/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

heights = "ESabcdefghijklmnopqrstuvwxyz"

class node:
    def __init__(self, xCord, yCord, height) -> None:
        self.xCord = xCord
        self.yCord = yCord
        self.dist = 99999999999999
        self.height = height
        self.hasBeenCurrent = False

    def __getitem__(self, pain):
        print(self)
        print(pain)
        return "self"

nodeDict = {}
start = ()
end = ()
for i in range(len(input)): #node array setup
    nodeDict[i] = {}
    for j in range(len(input[i])):
        nodeDict[i][j] = node(i, j, heights.index(input[i][j]))
        if input[i][j] == "S":
            start = (i, j)
            nodeDict[i][j].dist = 0
        if input[i][j] == "E":
            end = (i, j)

possibleNextCurrent = []
def checkNeighbor(current, side): #goto side
    if side.height <= current.height+1 and side.dist > current.dist:
        nodeDict[side.xCord][side.yCord].dist = current.dist+1
        
        for i in range(len(possibleNextCurrent)):
            if nodeDict[possibleNextCurrent[i].xCord][possibleNextCurrent[i].yCord].dist <= nodeDict[side.xCord][side.yCord].dist:
                possibleNextCurrent.insert(i, (side.xCord, side.yCord))

        if len(possibleNextCurrent) == 0:
            possibleNextCurrent.append((side.xCord, side.yCord))
        return True
    return False

current = start
while not current == end:
    print(current[0])
    currentNode = nodeDict[current[0]][current[1]]

    above = True
    below = True
    left = True
    right = True

    if current[0]-1 < 0:
        left = False
    if current[0]+1 > len(input[0]):
        right = False
    if current[1]-1 < 0:
        below = False
    if current[1]+1 > len(input):
        above = False

    possible = False
    if above:
        if left:
            sideNode = nodeDict[current[0]-1][current[1]+1]
            checkNeighbor(currentNode, sideNode)

        if right:
            sideNode = nodeDict[current[0]+1][current[1]+1]
            checkNeighbor(currentNode, sideNode)
        
        sideNode = nodeDict[current[0]][current[1]+1]
        checkNeighbor(currentNode, sideNode)
    
    if below:
        if left:
            sideNode = nodeDict[current[0]-1][current[1]-1]
            checkNeighbor(currentNode, sideNode)

        if right:
            sideNode = nodeDict[current[0]+1][current[1]-1]
            checkNeighbor(currentNode, sideNode)
        
        sideNode = nodeDict[current[0]][current[1]-1]
        checkNeighbor(currentNode, sideNode)
    
    if left:
        sideNode = nodeDict[current[0]-1][current[1]]
        checkNeighbor(currentNode, sideNode)

    if right:
        sideNode = nodeDict[current[0]+1][current[1]]
        checkNeighbor(currentNode, sideNode)

    current = possibleNextCurrent.pop()

print(current)
print(nodeDict[current[0]][current[1]])