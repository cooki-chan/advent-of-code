input = ""
with open('day8/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

def checkTreeScore(x:int, y:int):
    treeHeight = int(input[y][x])

    right = -1
    left = -1
    for i in range(len(input[y])):
        checkHeight = int(input[y][i])
        if checkHeight >= treeHeight:
            if i > x and right == -1: #ON RIGHT OF X, find first instance
                right = i - x
            elif i < x: #ON LEFT OF X, find last instance
                left = x - i
            #print(f"{i}, {x}")
    
    if right == -1:
        if x != len(input[y])-1:
            right = len(input[y])-1 - x
        else:
            right = 0
    if left == -1 :
        if x != 0:
            left = x
        else:
            left = 0

    top = -1
    bot = -1
    for i in range(len(input)):
        checkHeight = int(input[i][x])
        if checkHeight >= treeHeight:
            if i > y and bot == -1: #ON BOT OF X, find first instance
                bot = i - y
            elif i < y: #ON LTOP OF X, find last instance
                top = y - i
            #print(f"{i}, {x}")
    
    if bot == -1 :
        if y != len(input[y])-1:
            bot = len(input[y]) - 1 - y
        else:
            bot = 0
    if top == -1 :
        if y != 0:
            top = y
        else:
            top = 0

    return [right, left, bot, top]

highestTreeScore = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        treeScoreList = checkTreeScore(x, y)
        treeScore = treeScoreList[0] * treeScoreList[1] * treeScoreList[2] * treeScoreList[3]
        if treeScore > highestTreeScore:
            highestTreeScore = treeScore
        print(f"{str(x)}, {str(y)} = {input[y][x]}| {treeScoreList[0]} * {treeScoreList[1]} * {treeScoreList[2]} * {treeScoreList[3]}= {str(treeScore)}")

print(highestTreeScore)
