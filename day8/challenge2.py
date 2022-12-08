input = ""
with open('day8/exampleInp.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

def checkTreeScore(x:int, y:int):
    treeHeight = int(input[y][x])

    right = 0
    left = 0
    for i in range(len(input[y])):
        checkHeight = input[y][i]
        if checkHeight >= treeHeight:
            if i > x and right == 0: #ON RIGHT OF X, find first instance
                right = i
            elif i < x: #ON LEFT OF X, find last instance
                left = i
    
    if right == 0 and y != len(input[y])-1:
        right = len(input[y])-1 - x
    if left == 0 and y != 0:
        left = x + 1

highestTreeScore = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        treeScoreList = checkTreeScore(x, y)
        treeScore = treeScoreList[0] * treeScoreList[1] * treeScoreList[2] * treeScoreList[3]
        if treeScore > highestTreeScore:
            highestTreeScore = treeScore
        print(f"{str(x)}, {str(y)} = {input[y][x]}| {treeScoreList[0]} * {treeScoreList[1]} * {treeScoreList[2]} * {treeScoreList[3]} = {str(treeScore)}")

print(highestTreeScore)
