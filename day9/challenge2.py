import math

input = ""
with open('day9/inp1.txt') as i:
    input = i.readlines()
    for i in range(0, len(input)-1):
        input[i] = input[i].replace("\n", "")

head = [0, 0] #x, y
tails = []
for i in range(9):
    tails.append([0,0])

def moveTail():
    index = 0
    for index in range(len(tails)):
        comparedVal = []
        if index == 0:
            comparedVal = head
        else:
            comparedVal = tails[index-1]

        dist = math.sqrt((comparedVal[0] - tails[index][0])**2 + (comparedVal[1] - tails[index][1])**2) #dist formula

        if dist >= 2.0: #tail needs to move
            if comparedVal[1] > tails[index][1]:   #comparedVal is higher, tail must move up
                tails[index][1]+=1
            elif comparedVal[1] < tails[index][1]: #tail is higher, tail ust move down
                tails[index][1]-=1

            if comparedVal[0] > tails[index][0]:   #comparedVal is right, tail mush move right
                tails[index][0]+=1
            elif comparedVal[0] < tails[index][0]: #tail is right, tail must move left
                tails[index][0]-=1
        index+=1

tailVisited = set() #t

for i in input:
    command = i.split(" ")
    for i in range(int(command[1])):
        match command[0]:
            case "R":
                head[0]+=1
            case "L":
                head[0]-=1
            case "U":
                head[1]+=1
            case "D":
                head[1]-=1
        moveTail()
        tailVisited.add(tuple(tails[8]))

print(len(tailVisited))
    

