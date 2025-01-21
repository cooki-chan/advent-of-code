input = ""
with open('day8/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

def checkTreeVis(x:int, y:int):
    top = True
    bot = True
    left = True
    right = True

    currIndex = 0
    for i in input[y]:
        if int(i) >= int(input[y][x]):
            if currIndex > x:
                right = False
            elif currIndex < x:
                left = False
        currIndex += 1

    currIndex = 0
    for i in input:
        if int(i[x]) >= int(input[y][x]):
            if currIndex > y:
                bot = False
            elif currIndex < y:
                top = False
        currIndex += 1
    
    if bot or top or left or right:
        print(input[y][x])

    return bot or top or left or right

treeSeen = 0
for y in range(len(input)):
    for x in range(len(input[0])):
        if checkTreeVis(x, y):
            treeSeen += 1

print(treeSeen)
