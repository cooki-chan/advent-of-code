input = ""
with open('day12/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

heights = "ESabcdefghijklmnpqrstuvwxyz"

class node:
    def __init__(self, xCord, yCord, height) -> None:
        self.xCord = xCord
        self.yCord = yCord
        self.dist = 99999999999999
        self.height = height

nodeDict = {}
start, end = ()
for i in range(len(input)): #node array setup
    nodeDict[i] = {}
    for j in range(len(input[i])):
        if input[i][j] == "S":
            start = (i, j)
        if input[i][j] == "E":
            end = (i, j)
        nodeDict[i][j] = node(i, j, heights.index(input[i][j]))